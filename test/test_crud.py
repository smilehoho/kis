import uuid
from datetime import datetime, timedelta

import pytest
from sqlalchemy.orm import Session

from app import crud
from app.database import SessionLocal
from app.enums import AccessKeyStatusEnum
from app.models import Oauth2


@pytest.fixture
def db() -> Session:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture
def make_oauth2():
    def _make_oauth2(access_token: str) -> Oauth2:
        return Oauth2(
            access_token=access_token,
            access_token_token_expired=str(datetime.now() + timedelta(days=1)),
            token_type="Bearer",
            expires_in=86400,
        )

    return _make_oauth2


def test_create_oauth2(db, make_oauth2):
    # given
    access_token = str(uuid.uuid4())
    oauth2 = make_oauth2(access_token)

    # when
    crud.create_oauth2(db=db, oauth2=oauth2)

    # then
    assert oauth2.id > 0
    assert oauth2.access_token == access_token


def test_get_oauth2(db, make_oauth2):
    # given
    access_token = str(uuid.uuid4())
    oauth2 = make_oauth2(access_token)
    crud.create_oauth2(db=db, oauth2=oauth2)

    # when
    oauth2: Oauth2 = crud.get_oauth2(db)

    # then
    assert type(oauth2) is Oauth2
    assert oauth2.status == AccessKeyStatusEnum.active


def test_expire_all_access_key(db, make_oauth2):
    # given
    oauth2s = [make_oauth2("far"), make_oauth2("boo")]

    for oauth2 in oauth2s:
        crud.create_oauth2(db=db, oauth2=oauth2)

    # when
    rowcount = crud.expire_all_access_key(db=db)

    # then
    assert rowcount == len(oauth2s)

    for oauth2 in oauth2s:
        assert oauth2.status == AccessKeyStatusEnum.expired
