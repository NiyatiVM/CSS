import sqlite3 as lite
import sys


con = lite.connect('client.db')

# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE Clients")

with con:
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Clients(identity INTEGER PRIMARY KEY, functionnum INTEGER UNIQUE)")
    cur.execute("DELETE FROM Clients")
    con.commit()
    # cur.execute("SELECT * FROM Clients")
    # ans=cur.fetchall()
    # for i in ans:
    # 	print(i)
con = lite.connect('server.db')

# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE Servers")
with con:
    cur = con.cursor() 
    cur.execute("DELETE FROM Servers")
    #cur.execute("CREATE TABLE Servers(identity INTEGER PRIMARY KEY, functionnum INTEGER UNIQUE)")
