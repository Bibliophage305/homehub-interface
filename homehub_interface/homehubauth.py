import hashlib
import os
import random
from typing import Dict, Any, List, Union

from homehubrequest import HomeHubRequest


class AuthenticationException(Exception):
    pass


class HomeHubAuth:
    def __init__(self, session: Any) -> None:
        self.session: Any = session
        self.server_nonce: str = ""
        self.session_id: int = 0
        self.refresh_client_nonce()

    def refresh_client_nonce(self) -> None:
        self.client_nonce: int = random.randint(0, 1 << 31 - 1)

    @property
    def auth_hash(self) -> str:
        return self._md5_hex(f"{self.user}:{self.server_nonce}:{self.password}")

    def authenticate(self) -> None:
        print("authenticating with", self.user)

        request: HomeHubRequest = self.session.make_request(
            [
                {
                    "method": "logIn",
                    "parameters": {
                        "user": self.user,
                        "persistent": True,
                        "session-options": {
                            "nss": [
                                {
                                    "name": "gtw",
                                    "uri": "http://sagemcom.com/gateway-data",
                                }
                            ],
                            "language": "ident",
                            "context-flags": {
                                "get-content-name": True,
                                "local-time": True,
                            },
                            "capability-depth": 2,
                            "capability-flags": {
                                "name": True,
                                "default-value": False,
                                "restriction": True,
                                "description": False,
                            },
                            "time-format": "ISO_8601",
                        },
                    },
                }
            ]
        )

        if not request.is_successful:
            raise AuthenticationException(
                f"Failed to authenticate. Error: {request.response_json['reply']['error']['description']}"
            )

        params: Dict[str, Any] = request.response_json["reply"]["actions"][0][
            "callbacks"
        ][0]["parameters"]

        self.server_nonce = params["nonce"]
        self.session_id = params["id"]

    @property
    def auth_key(self) -> str:
        return self._md5_hex(
            f"{self.auth_hash}:{self.session.next_request_id}:{self.client_nonce}:JSON:/cgi/json-req"
        )

    def _md5_hex(self, s: str) -> str:
        return hashlib.md5(s.encode("utf-8")).hexdigest()

    @property
    def ha1(self) -> str:
        return self.auth_hash[:10] + self.password + self.auth_hash[10:]

    @property
    def auth_cookie(
        self,
    ) -> Dict[str, Union[int, str, bool, Dict[str, Union[str, List[Dict[str, str]]]]]]:
        return {
            "req_id": self.session.next_request_id + 1,
            "sess_id": self.session_id,
            "basic": False,
            "user": self.user,
            "dataModel": {
                "name": "Internal",
                "nss": [{"name": "gtw", "uri": "http://sagemcom.com/gateway-data"}],
            },
            "ha1": self.ha1,
            "nonce": self.server_nonce,
        }


class HomeHubAdminAuth(HomeHubAuth):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.user: str = "admin"
        raw_password: str = os.getenv("HOMEHUB_ADMIN_PASSWORD")
        if raw_password is None:
            raise ValueError("HOMEHUB_ADMIN_PASSWORD not set")
        self.password: str = self._md5_hex(raw_password)
        super().__init__(*args, **kwargs)


class HomeHubGuestAuth(HomeHubAuth):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.user: str = "guest"
        self.password: str = self._md5_hex("")
        super().__init__(*args, **kwargs)
