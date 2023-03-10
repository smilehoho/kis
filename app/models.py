from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class Oauth2(Base):
    __tablename__ = "oauth2"

    id = Column("oauth2_id", Integer, primary_key=True, autoincrement=True)
    access_token = Column(String, nullable=False, unique=True)
    access_token_token_expired = Column(String, nullable=False)
    token_type = Column(String, nullable=False)
    expires_in = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="active")
    created_at = Column(DateTime, nullable=False, default=datetime.now())
