import os
import json
from urllib.parse import urljoin
from typing import List, Dict, Union

from homehubauth import HomeHubGuestAuth, HomeHubAdminAuth
from homehubrequest import HomeHubRequest


class AuthenticationException(Exception):
    pass


class ResponseException(Exception):
    pass


class HomeHubSession:

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session_id: int = 0
        self._guest_authentication: Union[HomeHubGuestAuth, None] = None
        self._admin_authentication: Union[HomeHubAdminAuth, None] = None
        self.requests: List[HomeHubRequest] = []

    @property
    def host(self) -> str:
        return os.getenv("HOMEHUB_HOST", "192.168.1.254")

    @property
    def base_url(self) -> str:
        return f"http://{self.host}"

    @property
    def api_url(self) -> str:
        return urljoin(self.base_url, "/cgi/json-req")

    @property
    def authentication(self) -> Union[HomeHubGuestAuth, HomeHubAdminAuth, None]:
        if self._admin_authentication is not None:
            return self._admin_authentication
        if self._guest_authentication is not None:
            return self._guest_authentication
        return None

    @property
    def next_request_id(self) -> int:
        return len(self.requests)

    def uri_to_url(self, uri: str) -> str:
        return urljoin(self.base_url.rstrip("/"), uri)

    def authenticate_guest(self) -> None:
        self._guest_authentication = HomeHubGuestAuth(self)
        self._guest_authentication.authenticate()

    def authenticate_admin(self) -> None:
        reset_request = HomeHubRequest(self)

        reset_request.add_action({"method": "resetEvents"})

        reset_request.send()

        self.requests = []
        self.session_id = 0
        self._guest_authentication = None

        self._admin_authentication = HomeHubAdminAuth(self)
        self._admin_authentication.authenticate()

    def make_request(
        self, actions: List[Dict[str, Union[str, Dict[str, Union[str, bool]]]]]
    ) -> Dict[str, Union[str, Dict[str, Union[str, bool]]]]:
        if self.authentication is None:
            self.authenticate_guest()

        request = HomeHubRequest(self)

        for action in actions:
            request.add_action(action)

        request.send()

        self.requests.append(request)

        return json.loads(request.response.text)

    def get_hub_light_control(
        self,
    ) -> Dict[str, Union[str, Dict[str, Union[str, bool]]]]:
        actions = [
            {
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/LedEnable",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Brightness",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Schedule/Enable",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Schedule/TurnLightOn",
                "options": {"capability-flags": {"interface": True}},
            },
            {
                "method": "getValue",
                "xpath": "Device/Managers/HubLightControl/Schedule/TurnLightOff",
                "options": {"capability-flags": {"interface": True}},
            },
        ]

        data = self.make_request(actions)

        return data

    def get_devices(self) -> List[Dict[str, Union[str, Dict[str, Union[str, bool]]]]]:
        """
        Returns the list of connected devices

        :param only_active: a flag indicating whether only currently active (connected) devices should be returned.
        Default `True`
        :return: a dictionary containing all the devices connected to the bt home hub
        """

        actions = [
            {
                "method": "getValue",
                "xpath": "Device/Hosts/Hosts",
                "options": {"capability-flags": {"interface": True}},
            }
        ]

        data = self.make_request(actions)

        return data

    def get_vendor_log_download_uri(
        self,
    ) -> Dict[str, Union[str, Dict[str, Union[str, bool]]]]:
        actions = [
            {
                "method": "getVendorLogDownloadURI",
                "xpath": "Device/DeviceInfo/VendorLogFiles/VendorLogFile[@uid='1']",
                "parameters": {"FileName": "eventLog"},
            }
        ]

        data = self.make_request(actions)

        return data

    @staticmethod
    def _is_successful(
        data: Dict[str, Union[str, Dict[str, Union[str, bool]]]]
    ) -> bool:
        return (
            data and data.get("reply", {}).get("error", {}).get("code", {}) == 16777216
        )

    @staticmethod
    def _is_invalid_user_session(
        data: Dict[str, Union[str, Dict[str, Union[str, bool]]]]
    ) -> bool:
        return (
            data and data.get("reply", {}).get("error", {}).get("code", {}) == 16777219
        )

    @staticmethod
    def _parse_homehub_response(
        data: Dict[str, Union[str, Dict[str, Union[str, bool]]]]
    ) -> List[Dict[str, Union[str, bool]]]:
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
