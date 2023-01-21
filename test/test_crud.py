import pytest

from app import crud
from app.database import Session
from app.models import Oauth2
from app.enums import AccessKeyStatusEnum


@pytest.fixture
def db():
    session = Session()

    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture
def oauth2():
    return Oauth2(
        access_token="*****",
        access_token_token_expired="2023-01-10 10:50:00",
        token_type="Bearer",
        expires_in=86400,
    )


def test_create_access_key(db: Session, oauth2: Oauth2):
    crud.create_access_key(db=db, oauth2=oauth2)

    assert oauth2.id > 0
    assert oauth2.access_token == "*****"
    assert oauth2.status == AccessKeyStatusEnum.active


def test_get_access_key(db: Session, oauth2: Oauth2):
    crud.create_access_key(db=db, oauth2=oauth2)
    oauth2 = crud.get_access_key(db=db)

    assert type(oauth2) is Oauth2


def test_expire_all_access_key(db: Session, oauth2: Oauth2):
    crud.create_access_key(db=db, oauth2=oauth2)

    assert oauth2.status == AccessKeyStatusEnum.active

    rowcount = crud.expire_all_access_key(db=db)

    assert rowcount > 0
    assert oauth2.status == AccessKeyStatusEnum.expired
