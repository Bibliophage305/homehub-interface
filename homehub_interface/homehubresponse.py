import json

from requests import Response
from typing import List


class HomeHubResponse:
    def __init__(self, response: Response) -> None:
        self.response = response
        try:
            response_json = response.json()
        except Exception as e:
            print("error decoding json")
            print(response.text)
            raise e
        self.uid: int = response_json["reply"]["uid"]
        self.id: int = response_json["reply"]["id"]
        error = response_json["reply"]["error"]
        self.error = HomeHubResponseError(error["code"], error["description"])
        self.actions = []
        for action in response_json["reply"]["actions"]:
            uid = action["uid"]
            id = action["id"]
            error = action["error"]
            callbacks = action["callbacks"]
            self.actions.append(
                HomeHubActionResponse(
                    uid,
                    id,
                    HomeHubResponseError(error["code"], error["description"]),
                    [
                        HomeHubActionResponseCallback(
                            callback["uid"],
                            callback["result"],
                            callback["xpath"],
                            callback["parameters"],
                        )
                        for callback in callbacks
                    ],
                )
            )

    @property
    def is_successful(self) -> bool:
        return self.error.is_successful

    @property
    def has_invalid_user_session_error(self) -> bool:
        return self.error.is_invalid_user_session_error

    def __str__(self):
        lines = []
        lines.append(f"UID: {self.uid}")
        lines.append(f"ID: {self.id}")
        lines.append("Error:")
        lines.append(str(self.error))
        lines.append("Actions:")
        for action in self.actions:
            lines.append(str(action))
        return "\n".join(lines)


class HomeHubResponseError:
    def __init__(self, code: int, description: str) -> None:
        self.code = code
        self.description = description

    @property
    def is_ok(self) -> bool:
        return self.code == 16777216

    @property
    def is_applied(self) -> bool:
        return self.code == 16777238

    @property
    def is_successful(self) -> bool:
        return self.is_ok or self.is_applied

    @property
    def is_invalid_user_session_error(self) -> bool:
        return self.code == 16777219

    @property
    def is_action_error(self) -> bool:
        return self.code == 16777236

    @property
    def is_unknown_path_error(self) -> bool:
        return self.code == 16777242

    @property
    def is_invalid_request_format_error(self) -> bool:
        return self.code == 16777218

    @property
    def is_internal_error(self) -> bool:
        return self.code == 16777265

    def __str__(self):
        lines = []
        lines.append(f"Code: {self.code}")
        lines.append(f"Description: {self.description}")
        return "\n".join(lines)


class HomeHubActionResponseCallback:
    def __init__(self, uid: int, result: dict, xpath: str, parameters: dict) -> None:
        self.uid = uid
        self.result = result
        self.xpath = xpath
        self.parameters = parameters

    def __str__(self):
        lines = []
        lines.append(f"UID: {self.uid}")
        lines.append("Result:")
        lines.append(json.dumps(self.result, indent=4))
        lines.append(f"Xpath: {self.xpath}")
        lines.append("Parameters:")
        lines.append(json.dumps(self.parameters, indent=4))
        return "\n".join(lines)


class HomeHubActionResponse:
    def __init__(
        self,
        uid: int,
        id: int,
        error: HomeHubResponseError,
        callbacks: List[HomeHubActionResponseCallback],
    ) -> None:
        self.uid = uid
        self.id = id
        self.error = error
        self.callbacks = callbacks

    @property
    def is_successful(self) -> bool:
        return self.error.is_successful

    def __str__(self):
        lines = []
        lines.append(f"UID: {self.uid}")
        lines.append(f"ID: {self.id}")
        lines.append("Error:")
        lines.append(str(self.error))
        lines.append("Callbacks:")
        for callback in self.callbacks:
            lines.append(str(callback))
        return "\n".join(lines)
