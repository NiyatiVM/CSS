import sqlite3 as lite
import sys


con = lite.connect('client.db')

# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE Clients")

with con:
    cur = con.cursor()    
    cur.execute("CREATE TABLE Clients(identity INTEGER PRIMARY KEY, functionnum INTEGER UNIQUE)")

con = lite.connect('server.db')

# with con:
with con:
    cur = con.cursor() 
    #cur.execute("DELETE FROM Servers")
    cur.execute("CREATE TABLE Servers(identity INTEGER PRIMARY KEY, functionnum INTEGER UNIQUE)")
