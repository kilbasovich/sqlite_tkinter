import sqlite3
from sqlite3.dbapi2 import connect

connect_db = sqlite3.connect('test.db')
cursor = connect_db.cursor()
cursor.execute("DROP TABLE IF EXISTS table_users")
query_create_table = '''CREATE TABLE table_users (
person_id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR NOT NULL,
name2 VARCHAR NOT NULL,
tel INT DEFAULT 0,
data_visit datetime
);'''

cursor.execute(query_create_table)
connect_db.commit()
cursor.close()