from dotenv import dotenv_values

from api import Api
from config import Config


def main():
    env = dotenv_values(".env")
    api = Api(appkey=env["appkey"], secretkey=env["secretkey"], config=Config)

    # print(api.approval())
    print(api.hashkey(contents={"STRING": "1234", "INT": 1234}))


if __name__ == "__main__":
    main()
