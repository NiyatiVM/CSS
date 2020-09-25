import sqlite3

try:
    sqliteConnection = sqlite3.connect('Clients.db')
    sqlite_create_table_query = '''CREATE TABLE Clients (
                                identity INTEGER PRIMARY KEY,
                                functionnum INTEGER NOT NULL UNIQUE);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")