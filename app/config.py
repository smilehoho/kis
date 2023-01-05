class Config:
    DOMAIN: str = "https://openapi.koreainvestment.com:9443"


class DevConfig(Config):
    DOMAIN: str = "https://openapivts.koreainvestment.com:29443"
