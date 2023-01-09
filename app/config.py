class Config:
    DOMAIN: str = "https://openapi.koreainvestment.com:9443"
    SQLITE3_DATABASE_FILE: str = "example.db"


class DevConfig(Config):
    DOMAIN: str = "https://openapivts.koreainvestment.com:29443"
