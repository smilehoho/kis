import requests
from config import Config


class Api:
    def __init__(self, appkey: str, secretkey: str, config: Config) -> None:
        self.appkey = appkey
        self.secretkey = secretkey
        self.config = config
        self.approval_key: str | None = None
        self.access_token: str = ""

    def approval(self) -> str | None:
        """실시간 (웹소켓) 접속키 발급받으실 수 있는 API 입니다.
        웹소켓 이용 시 해당 키를 appkey와 appsecret 대신 헤더에 넣어 API를 호출합니다.
        """
        response = requests.post(
            url=self.config.DOMAIN + "/oauth2/Approval",
            headers={"Content-Type": "application/json; utf-8"},
            json={
                "grant_type": "client_credentials",
                "appkey": self.appkey,
                "secretkey": self.secretkey,
            },
        )

        data = response.json()
        self.approval_key = data["approval_key"]

        return self.approval_key

    def hashkey(self, contents: dict) -> str:
        """해쉬키(Hashkey)는 보안을 위한 요소로 사용자가 보낸 요청 값을 중간에 탈취하여 변조하지 못하도록 하는데 사용됩니다.
        보안을 위해 POST로 보내는 요청(주로 주문/정정/취소 API 해당)은 사전에 body 값 암호화가 필요하며,
        이 때 hashkey를 활용한 암호화를 진행합니다.
        """
        response = requests.post(
            url=self.config.DOMAIN + "/uapi/hashkey",
            headers={
                "Content-Type": "application/json; utf-8",
                "appkey": self.appkey,
                "appsecret": self.secretkey,
            },
            json=contents,
        )

        data = response.json()

        return data["HASH"]

    def tokenp(self) -> str:
        """본인 계좌에 필요한 인증 절차로, 인증을 통해 접근 토큰을 부여받아 오픈API 활용이 가능합니다."""
        response = requests.post(
            url=self.config.DOMAIN + "/oauth2/tokenP",
            headers={
                "Content-Type": "application/json; utf-8",
            },
            json={
                "grant_type": "client_credentials",
                "appkey": self.appkey,
                "appsecret": self.secretkey,
            },
        )

        data = response.json()
        self.access_token = data["access_token"]

        return self.access_token
