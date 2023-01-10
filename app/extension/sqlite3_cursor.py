import sqlite3
from app.config import DevConfig as Config

DATABASE_FILE_DIRECTORY: str = "db/"

con = sqlite3.connect(DATABASE_FILE_DIRECTORY + Config.SQLITE3_DATABASE_FILE)
cur = con.cursor()

