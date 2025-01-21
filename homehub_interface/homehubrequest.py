import json
import requests
from urllib.parse import quote
from typing import Dict, Any, List

from homehubaction import HomeHubAction


class HomeHubRequest:
    def __init__(self, session: Any) -> None:
        self.session: Any = session
        self.actions: List[HomeHubAction] = []
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
        return any(action.method == "logIn" for action in self.actions)

    @property
    def request_data(self) -> Dict[str, Any]:
        return {
            "request": {
                "actions": [action.as_dict() for action in self.actions],
                "auth-key": self.session.auth.auth_key,
                "cnonce": self.session.auth.client_nonce,
                "id": self.session.next_request_id,
                "priority": self.is_priority,
                "session-id": self.session.auth.session_id,
            }
        }

    def add_action(self, action: HomeHubAction) -> None:
        action.set_id(len(self.actions))
        self.actions.append(action)

    def send(self) -> None:
        self.session.auth.refresh_client_nonce()

        data = {"req": json.dumps(self.request_data, sort_keys=True).encode("utf-8")}

        try:
            self.response = requests.post(
                url=self.session.api_url,
                data=data,
                cookies=self.cookies,
                timeout=self.session.timeout,
            )
        except requests.Timeout:
            self.response = None

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
