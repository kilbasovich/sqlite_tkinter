import sqlite3

def sel():
    connect_db = sqlite3.connect('test.db')
    cursor = connect_db.cursor()
    select = '''SELECT * FROM table_users;'''
    cursor.execute(select)
    record = cursor.fetchall()
    print(record)
    connect_db.close()
    return record

if __name__ == '__main__':
    sel()    