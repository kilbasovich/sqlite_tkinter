from os import close
import sqlite3
from sqlite3.dbapi2 import connect

def ins_in(names):
    connect_db = sqlite3.connect('test.db')
    cursor = connect_db.cursor()
    inset = 'INSERT INTO table_users (name, name2, tel, data_visit) VALUES(?, ?, ?, ?);'
    cursor.execute(inset, names)
    connect_db.commit()
    connect_db.close()

if __name__ == '__main__':
    ins_in()