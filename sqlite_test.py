import sqlite3

try:
    sqlite_connection = sqlite3.connect('test.db')
    cursor = sqlite_connection.cursor()
    print('test.db connect!!!')

    sqlite_select_query = 'select sqlite_version();'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print('version test.db', record)
    cursor.close()

except sqlite3.Error as error:
    print('error! ', error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print('connection close!!!')