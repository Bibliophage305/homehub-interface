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
        self.requests: List[HomeHubRequest] = []
        self.next_request_id: int = 0
        self.auth = None

    @property
    def host(self) -> str:
        return os.getenv("HOMEHUB_HOST", "192.168.1.254")

    @property
    def base_url(self) -> str:
        return f"http://{self.host}"

    @property
    def api_url(self) -> str:
        return urljoin(self.base_url, "/cgi/json-req")

    def uri_to_url(self, uri: str) -> str:
        return urljoin(self.base_url.rstrip("/"), uri)

    def authenticate_guest(self) -> None:
        self.auth = HomeHubGuestAuth(self)
        self.auth.authenticate()

    def authenticate_admin(self) -> None:
        self.make_request([{"method": "resetEvents"}])

        self.next_request_id = 0

        self.session_id = 0

        self.auth = HomeHubAdminAuth(self)
        self.auth.authenticate()

    def make_request(
        self, actions: List[Dict[str, Union[str, Dict[str, Union[str, bool]]]]]
    ) -> Dict[str, Union[str, Dict[str, Union[str, bool]]]]:
        if self.auth is None:
            self.authenticate_guest()

        request = HomeHubRequest(self)

        for action in actions:
            request.add_action(action)

        request.send()

        self.requests.append(request)

        self.next_request_id += 1

        return request

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

        request = self.make_request(actions)

        return request.response_json

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

        request = self.make_request(actions)

        return request.response_json

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

        request = self.make_request(actions)

        return request.response_json

    @staticmethod
    def _is_invalid_user_session(
        data: Dict[str, Union[str, Dict[str, Union[str, bool]]]]
    ) -> bool:
        return (
            data and data.get("reply", {}).get("error", {}).get("code", {}) == 16777219
        )
