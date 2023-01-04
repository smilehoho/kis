import requests
import json

from config import Config


class Api:
    def __init__(self, appkey: str, secretkey: str, config: Config) -> None:
        self.appkey = appkey
        self.secretkey = secretkey
        self.config = config

    def approval(self) -> str:
        response = requests.post(
            url=self.config.DOMAIN + "/oauth2/Approval",
            headers={"Content-Type": "application/json; utf-8"},
            json={
                "grant_type": "client_credentials",
                "appkey": self.appkey,
                "secretkey": self.secretkey,
            },
        )

        data = json.loads(response.text)
        self.approval_key = data["approval_key"]

        return self.approval_key

    def hashkey(self, contents: dict) -> str:
        response = requests.post(
            url=self.config.DOMAIN + "/uapi/hashkey",
            headers={
                "Content-Type": "application/json; utf-8",
                "appkey": self.appkey,
                "appsecret": self.secretkey,
            },
            json=contents,
        )

        data = json.loads(response.text)

        return data["HASH"]
