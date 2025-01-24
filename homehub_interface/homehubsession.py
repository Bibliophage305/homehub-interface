import os
from urllib.parse import urljoin
from typing import List, Dict, Union

from homehubauth import HomeHubGuestAuth, HomeHubAdminAuth
from homehubrequest import HomeHubRequest
from homehubaction import *


class AuthenticationException(Exception):
    pass


class ResponseException(Exception):
    pass


class HomeHubSession:

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
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

    def reauthenticate(self) -> None:
        if self.auth.is_admin:
            self.authenticate_admin()
        else:
            self.authenticate_guest()

    def reset_session(self) -> None:
        self.make_request([HomeHubActionResetEvents()])
        self.next_request_id = 0

    def authenticate_guest(self) -> None:
        self.auth = HomeHubGuestAuth(self)
        self.auth.authenticate()

    def authenticate_admin(self) -> None:
        if self.auth is None:
            self.authenticate_guest()
        self.reset_session()
        self.auth = HomeHubAdminAuth(self)
        self.auth.authenticate()

    def make_request(self, actions: List[HomeHubAction], auth_is_fresh = False) -> HomeHubRequest:
        request = HomeHubRequest(self)

        admin_required = False

        for action in actions:
            request.add_action(action)
            if action.admin_required:
                admin_required = True

        if admin_required and not self.auth.is_admin:
            raise AuthenticationException("Admin privileges required")

        request.send()

        if request.has_invalid_user_session_error:
            if auth_is_fresh:
                raise AuthenticationException("Failed to reauthenticate")
            self.reauthenticate()
            return self.make_request(actions, auth_is_fresh=True)

        self.requests.append(request)

        self.next_request_id += 1

        return request
