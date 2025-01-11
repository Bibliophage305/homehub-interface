import os
import requests
import json
from urllib.parse import quote

from homehubauth import HomeHubGuestAuth, HomeHubAdminAuth
from homehubrequest import HomeHubRequest


class AuthenticationException(Exception):
    pass


class ResponseException(Exception):
    pass


class HomeHubSession:

    def __init__(self, timeout=10):
        self.timeout = timeout
        self.session_id = 0
        self._guest_authentication = None
        self._admin_authentication = None
        self.requests = []

    @property
    def host(self):
        return os.getenv("HOMEHUB_HOST", "192.168.1.254")

    @property
    def url(self):
        return f"http://{self.host}/cgi/json-req"

    @property
    def _authentication(self):
        if self._admin_authentication is not None:
            return self._admin_authentication
        if self._guest_authentication is not None:
            return self._guest_authentication
        return None
    
    @property
    def next_request_id(self):
        return len(self.requests)

    def authenticate_guest(self):
        """
        Authenticates the client by creating a new session. The session is automatically renewed so
        there is no need to authenticate again, unless an explicit AuthenticationException is thrown.
        """
        self._guest_authentication = HomeHubGuestAuth(self)
        # self.session_id = self._guest_authentication.session_id
        self.requests.append(None)

    def authenticate_admin(self):
        self._admin_authentication = HomeHubAdminAuth(self)

    def make_request(self, actions, admin_required=False):
        if self._authentication is None:
            self.authenticate_guest()

        headers = {
            "Cookie": "lang=en; session="
            + quote(json.dumps(self._authentication.auth_cookie).encode("utf-8"))
        }

        print("old method cookie")
        print(self._authentication.auth_cookie)
        print()

        request_data = self._authentication.request_object

        request_data["request"]["actions"] = actions

        print("old method request data")
        print(request_data)
        print()

        request = "req=" + quote(
            json.dumps(request_data, sort_keys=True).encode("utf-8")
        )

        response = requests.post(
            url=self.url, data=request, headers=headers, timeout=self.timeout
        )
        if response.status_code == 401:
            raise AuthenticationException("Session expired")
        elif response.status_code != 200:
            raise ResponseException("Failed, got a %s" % response.status_code)

        data = json.loads(response.text)
        if not self._is_successful(data):
            if self._is_invalid_user_session(data):
                self.authenticate_guest()
            raise ResponseException(
                "Failed. Reason: %s" % data["reply"]["error"]["description"]
            )

        # We don't let the request id grow exponentially
        if self._authentication.request_id > 100000:
            self.authenticate_guest()
            self._authentication.request_id = 0

        return data

    def get_hub_light_control(self):
        actions = [
            {
                "id": 0,
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/LedEnable",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "id": 1,
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Brightness",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "id": 2,
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Schedule/Enable",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "id": 3,
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Schedule/TurnLightOn",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "id": 4,
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Schedule/TurnLightOff",
                "options": {"capability-flags": {"interface": True}},
            },
        ]

        request = HomeHubRequest(
            len(self.requests),
            self.session_id,
            self.timeout,
            self.url,
            self._guest_authentication,
        )

        for action in actions:
            request.add_action(action)

        request.send()

        self.requests.append(request)

        return json.loads(request.response.text)

    def get_devices(self) -> list:
        """
        Returns the list of connected devices

        :param only_active: a flag indicating whether only currently active (connected) devices should be returned.
        Default `True`
        :return: a dictionary containing all the devices connected to the bt home hub
        """

        actions = [
            {
                "id": 0,
                "method": "getValue",
                "xpath": "Device/Hosts/Hosts",
                "options": {"capability-flags": {"interface": True}},
            }
        ]

        data = self.make_request(actions)

        return self._parse_homehub_response(data)

    @staticmethod
    def _is_successful(data):
        return (
            data and data.get("reply", {}).get("error", {}).get("code", {}) == 16777216
        )

    @staticmethod
    def _is_invalid_user_session(data):
        return (
            data and data.get("reply", {}).get("error", {}).get("code", {}) == 16777219
        )

    @staticmethod
    def _parse_homehub_response(data):
        """Parse the BT Home Hub data format."""
        known_devices = data["reply"]["actions"][0]["callbacks"][0]["parameters"][
            "value"
        ]

        devices = []

        for device in known_devices:
            # device = Device(
            #     mac_address=device["PhysAddress"].upper(),
            #     ip_address=device["IPAddress"],
            #     address_source=device["AddressSource"],
            #     name=device["UserHostName"] or device["HostName"],
            #     interface=device["InterfaceType"],
            #     active=device["Active"],
            #     user_friendly_name=device["UserFriendlyName"],
            #     detected_device_type=device["DetectedDeviceType"],
            #     user_device_type=device["UserDeviceType"],
            # )

            devices.append(device)

        return devices
