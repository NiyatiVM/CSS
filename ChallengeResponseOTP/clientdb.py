import random
import sqlite3

def adddetails(identity,functionnum):
	try:
		sqliteconn=sqlite3.connect('server.db')
		sqlitequery='INSERT INTO Servers(identity,functionnum) VALUES (?,?)'
		cursor=sqliteconn.cursor()
		data=(identity,functionnum)
		cursor.execute(sqlitequery,data)
		sqliteconn.commit()
		print("Reached")
		sqlitequery='SELECT functionnum FROM Servers WHERE identity=?'
		print("Here")
		cursor.execute(sqlitequery,(identity,))
		print("Then")
		ans=cursor.fetchone()
		print("Here")
		print("Entry:")
		print(ans[0])
		print("Successfully added entry")
		cursor.close()
	except:
		print("Could not add details")

	# conns[identity]=functionnum

def getdetails(serveridentity):
	try:
		sqliteconn=sqlite3.connect('server.db')
		sqlitequery='SELECT functionnum FROM Servers WHERE identity=?'
		cursor=sqliteconn.cursor()
		cursor.execute(sqlitequery,(serveridentity,))
		ans=cursor.fetchone()
		cursor.close()
		print(ans)
		if len(ans)>0:
			return ans[0]
		return random.randint(0,9)
	except:
		print("Could not get server")
		return random.randint(0,9)

	# if identity not in conns:
	# 	return random.randint(0,9)
	# return conns[identity]