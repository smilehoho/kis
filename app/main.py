import logging
from http.client import HTTPConnection

from api import Api
from config import DevConfig as Config
from dotenv import dotenv_values


def init_logging():
    """https://stackoverflow.com/questions/16337511/log-all-requests-from-the-python-requests-module"""
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    request_log = logging.getLogger("requests.packages.urllib3")
    request_log.setLevel(logging.DEBUG)
    request_log.propagate = True


def main():
    env = dotenv_values(".env")
    api = Api(appkey=env["appkey"], secretkey=env["secretkey"], config=Config)

    api.approval()
    # print(api.hashkey(contents={"STRING": "1234", "INT": 1234}))
    # print(api.tokenp())


if __name__ == "__main__":
    init_logging()
    main()
