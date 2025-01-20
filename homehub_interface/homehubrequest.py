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
                    json.dumps(self.session.auth.auth_cookie).encode("utf-8")
                ),
            }
            if self.session.auth is not None
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
                "session-id": self.session.auth.session_id,
                "priority": self.is_priority,
                "actions": [],
                "cnonce": self.session.auth.client_nonce,
                "auth-key": self.session.auth.auth_key,
                "actions": self.actions,
            }
        }

    def add_action(self, action: Dict[str, Union[str, int]]) -> None:
        self.actions.append(action | {"id": len(self.actions)})

    def send(self) -> None:
        self.session.auth.refresh_client_nonce()

        data = {"req": json.dumps(self.request_data, sort_keys=True).encode("utf-8")}

        self.response = requests.post(
            url=self.session.api_url,
            data=data,
            cookies=self.cookies,
            timeout=self.session.timeout,
        )

    @property
    def response_json(self) -> str:
        return json.loads(self.response.text) if self.response is not None else None

    @property
    def is_successful(self) -> bool:
        return (
            self.response_json
            and self.response_json.get("reply", {}).get("error", {}).get("code", {})
            == 16777216
        )
