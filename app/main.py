import logging

from dotenv import dotenv_values

from app.api import Api
from app.config import DevConfig as Config

logger = logging.getLogger(__name__)


def init_db():
    import app.models  # noqa
    from app.database import Base, engine

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def main():
    env = dotenv_values(".env")
    api = Api(appkey=env["appkey"], secretkey=env["secretkey"], config=Config)  # noqa

    # logger.debug(api.approval())
    # logger.debug(api.hashkey(contents={"STRING": "1234", "INT": 1234}))
    # logger.debug(api.tokenp())


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)

    init_db()
    main()
