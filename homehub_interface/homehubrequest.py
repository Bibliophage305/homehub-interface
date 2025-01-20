import json
import requests
from urllib.parse import quote
from typing import Dict, Any, List, Union


class HomeHubRequest:
    def __init__(self, session: Any) -> None:
        self.session: Any = session
        self.actions: List[Dict[str, Union[str, int]]] = []
        self.response: Any = None

    @property
    def cookies(self) -> Dict[str, str]:
        return (
            {
                "lang": "en",
                "session": quote(
                    json.dumps(self.session.authentication.auth_cookie).encode("utf-8")
                ),
            }
            if self.session.authentication is not None
            else {}
        )

    @property
    def is_priority(self) -> bool:
        return any(action["method"] == "logIn" for action in self.actions)

    @property
    def request_data(self) -> Dict[str, Any]:
        return {
            "request": {
                "id": self.session.next_request_id,
                "session-id": self.session.session_id,
                "priority": self.is_priority,
                "actions": [],
                "cnonce": self.session.authentication.client_nonce,
                "auth-key": self.session.authentication.auth_key,
                "actions": self.actions,
            }
        }

    def add_action(self, action: Dict[str, Union[str, int]]) -> None:
        self.actions.append(action | {"id": len(self.actions)})

    def send(self) -> None:
        self.session.authentication.refresh_client_nonce()

        data = {"req": json.dumps(self.request_data, sort_keys=True).encode("utf-8")}

        self.response = requests.post(
            url=self.session.api_url,
            data=data,
            cookies=self.cookies,
            timeout=self.session.timeout,
        )
