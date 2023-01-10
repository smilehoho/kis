import sqlalchemy
from sqlalchemy import create_engine
import datetime


engine = create_engine("sqlite:///db/example.db", echo=True, future=True)

from sqlalchemy import Column, Integer, MetaData, String, Table, DateTime, func

metadata = MetaData()


oauth2 = Table(
    "oauth2",
    metadata,
    Column("oauth2_id", Integer, primary_key=True),
    Column("access_token", String, nullable=False),
    Column("access_token_token_expired", String, nullable=False),
    Column("token_type", String, nullable=False),
    Column("expires_in", Integer, nullable=False),
    Column("status", String, nullable=False, server_default="active"),
    Column(
        "created_at",
        DateTime,
        nullable=False,
        server_default=func.datetime("now", "localtime"),
    ),
    sqlite_autoincrement=True,
)


members = Table(
    "members",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

metadata.drop_all(engine)
metadata.create_all(engine)

ins = oauth2.insert().values(
    access_token="test",
    access_token_token_expired="2023-01-10 10:50:00",
    token_type="Bearer",
    expires_in=86400,
)

conn = engine.connect()
result = conn.execute(ins)
conn.commit()

sel = oauth2.select()
result = conn.execute(sel)

for row in result:
    print(row)

if __name__ == "__main__":
    ...
