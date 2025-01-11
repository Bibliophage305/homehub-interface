import json
import requests
import math
import random
from urllib.parse import quote


class HomeHubRequest:
    def __init__(
        self, request_id, session_id, timeout, url, guest_auth, admin_auth=None
    ):
        self.request_id = request_id
        self.session_id = session_id
        self.timeout = timeout
        self.url = url
        self.guest_auth = guest_auth
        self.admin_auth = admin_auth
        self.actions = []
        self.response = None
        self.client_nonce = str(math.floor(4294967295 * (random.uniform(0, 1))))

    @property
    def auth(self):
        if self.admin_auth is not None:
            return self.admin_auth
        return self.guest_auth

    @property
    def auth_cookie(self):
        return {
            "req_id": self.request_id,
            "sess_id": self.session_id,
            "basic": False,
            "user": self.auth.user,
            "dataModel": {
                "name": "Internal",
                "nss": [{"name": "gtw", "uri": "http://sagemcom.com/gateway-data"}],
            },
            "ha1": self.auth.ha1,
            "nonce": self.auth.server_nonce,
        }

    @property
    def headers(self):
        if self.auth is not None:
            return {
                "Cookie": "lang=en; session="
                + quote(json.dumps(self.auth.auth_cookie).encode("utf-8"))
            }
        return {}

    @property
    def is_priority(self):
        return any(action["method"] == "login" for action in self.actions)

    @property
    def request_data(self):
        return {
            "request": {
                "id": self.request_id,
                "session-id": self.session_id,
                "priority": self.is_priority,
                "actions": [],
                "cnonce": self.auth.client_nonce,
                "auth-key": self.auth.auth_key,
                "actions": self.actions,
            }
        }

    def add_action(self, action):
        self.actions.append(action)

    def send(self):
        self.auth.client_nonce = self.client_nonce
        self.auth.request_id = self.request_id

        request = "req=" + quote(
            json.dumps(self.request_data, sort_keys=True).encode("utf-8")
        )

        self.response = requests.post(
            url=self.url, data=request, headers=self.headers, timeout=self.timeout
        )
