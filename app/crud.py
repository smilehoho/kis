from sqlalchemy.orm import Session
from models import Oauth2


def get_aaccess_key(db: Session):
    return db.query(Oauth2).filter(Oauth2.status == "active").one_or_none()


def create_access_key(db: Session, oauth2: Oauth2):
    db.add(oauth2)
    db.flush()
    db.refresh(oauth2)

    return oauth2
