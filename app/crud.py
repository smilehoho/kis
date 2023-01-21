from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.enums import AccessKeyStatusEnum
from app.models import Oauth2


def get_oauth2(db: Session) -> Oauth2 | None:
    return (
        db.execute(select(Oauth2).filter_by(status=AccessKeyStatusEnum.active))
        .scalars()
        .one_or_none()
    )


def create_oauth2(db: Session, oauth2: Oauth2) -> Oauth2:
    db.add(oauth2)
    db.flush()
    db.refresh(oauth2)

    return oauth2


def expire_all_access_key(db: Session) -> int:
    return db.execute(
        update(Oauth2)
        .where(Oauth2.status == AccessKeyStatusEnum.active)
        .values(status=AccessKeyStatusEnum.expired)
    ).rowcount
