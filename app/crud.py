from sqlalchemy.orm import Session
from app.models import Oauth2
from app.enums import AccessKeyStatusEnum
from sqlalchemy import select


def get_access_key(db: Session) -> Oauth2 | None:
    stmt = select(Oauth2).filter_by(status=AccessKeyStatusEnum.active)
    return db.execute(stmt).scalars().one_or_none()


def create_access_key(db: Session, oauth2: Oauth2) -> Oauth2:
    db.add(oauth2)
    db.flush()
    db.refresh(oauth2)

    return oauth2


def expire_all_access_key(db: Session) -> int:
    return db.query(Oauth2).update({Oauth2.status: AccessKeyStatusEnum.expired})
