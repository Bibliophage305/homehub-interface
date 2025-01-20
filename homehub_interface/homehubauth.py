import hashlib
import os
import random
import json
from homehubrequest import HomeHubRequest


class AuthenticationException(Exception):
    pass


class HomeHubAuth:

    def __init__(self, session):
        self.session = session
        self.server_nonce = None
        self.refresh_client_nonce()

    def refresh_client_nonce(self):
        self.client_nonce = random.randint(0, 1 << 31 - 1)

    @property
    def auth_hash(self):
        return self._md5_hex(
            f"{self.user}:{self.server_nonce if self.server_nonce is not None else ''}:{self.password}"
        )

    def authenticate(self):
        print("authenticating with", self.user)

        data = self.session.make_request(
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

        if not self._is_successful(data):
            raise AuthenticationException(
                f"Failed to authenticate. Error: {data['reply']['error']['description']}"
            )

        self.server_nonce = data["reply"]["actions"][0]["callbacks"][0]["parameters"][
            "nonce"
        ]
        self.session.session_id = data["reply"]["actions"][0]["callbacks"][0][
            "parameters"
        ]["id"]

    @property
    def auth_key(self):
        return self._md5_hex(
            f"{self.auth_hash}:{self.session.next_request_id}:{self.client_nonce}:JSON:/cgi/json-req"
        )

    @staticmethod
    def _is_successful(data):
        return (
            data and data.get("reply", {}).get("error", {}).get("code", {}) == 16777216
        )

    @staticmethod
    def _md5_hex(s):
        return hashlib.md5(s.encode("utf-8")).hexdigest()

    @property
    def ha1(self):
        return self.auth_hash[:10] + self.password + self.auth_hash[10:]

    @property
    def auth_cookie(self):
        return {
            "req_id": self.session.next_request_id + 1,
            "sess_id": self.session.session_id,
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
    def __init__(self, *args, **kwargs):
        self.user = "admin"
        raw_password = os.getenv("HOMEHUB_ADMIN_PASSWORD")
        if raw_password is None:
            raise ValueError("HOMEHUB_ADMIN_PASSWORD not set")
        self.password = self._md5_hex(raw_password)
        super().__init__(*args, **kwargs)


class HomeHubGuestAuth(HomeHubAuth):
    def __init__(self, *args, **kwargs):
        self.user = "guest"
        self.password = self._md5_hex("")
        super().__init__(*args, **kwargs)
