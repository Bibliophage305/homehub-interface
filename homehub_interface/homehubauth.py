import hashlib
import math
import os
import random
import json
import requests
from urllib.parse import quote


class AuthenticationException(Exception):
    pass


class HomeHubAuth:
    @property
    def auth_request_cookie(self):
        return {
            "req_id": 1,
            "sess_id": 0,
            "basic": False,
            "user": self.user,
            "dataModel": {
                "name": "Internal",
                "nss": [{"name": "gtw", "uri": "http://sagemcom.com/gateway-data"}],
            },
            "ha1": self.auth_key[:10] + self.password + self.auth_key[10:],
            # "ha1": "ca6e4940afd41d8cd98f00b204e9800998ecf8427e830e7a046fd8d92ecec8e4",
            "nonce": "",
        }

    @property
    def auth_request_data(self):
        return {
            "request": {
                "id": 0,
                "session-id": 0,
                "priority": True,
                "actions": [
                    {
                        "id": 0,
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
                ],
                "cnonce": 745670196,
                "auth-key": "06a19e589dc848a89675748aa2d509b3",
            }
        }

    def __init__(
        self,
        session
    ):
        self.client_nonce = str(math.floor(4294967295 * (random.uniform(0, 1))))
        self.server_nonce = None
        self.session = session
        self.authenticate()

    @property
    def auth_hash(self):
        return self._md5_hex(
            f"{self.user}:{self.server_nonce if self.server_nonce is not None else ''}:{self.password}"
        )

    def authenticate(self):
        print("authenticating with", self.user)
        headers = {
            "Cookie": "lang=en; session="
            + quote(json.dumps(self.auth_request_cookie).encode("utf-8"))
        }

        request = "req=" + quote(
            json.dumps(self.auth_request_data, sort_keys=True).encode("utf-8")
        )

        response = requests.post(
            self.session.url, data=request, headers=headers, timeout=self.session.timeout
        )
        data = json.loads(response.text)
        if response.status_code != 200:
            raise AuthenticationException(
                "Failed to authenticate. Status code: %s" % response.status_code
            )
        if not self._is_successful(data):
            raise AuthenticationException(
                "Failed to authenticate. Error: %s"
                % data["reply"]["error"]["description"]
            )

        self.server_nonce = data["reply"]["actions"][0]["callbacks"][0]["parameters"][
            "nonce"
        ]
        self.session.session_id = data["reply"]["actions"][0]["callbacks"][0]["parameters"][
            "id"
        ]

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
        return self.auth_key[:10] + self.password + self.auth_key[10:]

    @property
    def auth_cookie(self):
        return {
            "req_id": self.session.next_request_id,
            "sess_id": self.session.session_id,
            "basic": False,
            "user": self.user,
            "dataModel": {
                "name": "Internal",
                "nss": [{"name": "gtw", "uri": "http://sagemcom.com/gateway-data"}],
            },
            "ha1": self.auth_key[:10] + self.password + self.auth_key[10:],
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
