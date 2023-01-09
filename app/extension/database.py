import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/example.db", echo=True, future=True)

from sqlalchemy import Column, Integer, MetaData, String, Table

meta = MetaData()

members = Table(
    "members",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

meta.create_all(engine)

ins = members.insert().values(name="RM", age=26)

conn = engine.connect()
result = conn.execute(ins)

conn.execute(
    members.insert(),
    [
        {"name": "Jin", "age": 28},
        {"name": "Suga", "age": 27},
        {"name": "J-Hope", "age": 26},
        {"name": "Jimin", "age": 25},
        {"name": "V", "age": 25},
        {"name": "Jungkook", "age": 23},
    ],
)

sel = members.select()
result = conn.execute(sel)

for row in result:
    print(row)

if __name__ == "__main__":
    ...
