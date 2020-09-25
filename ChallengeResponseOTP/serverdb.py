import random
import sqlite3 as lite
clients={}
from functionlibrary import add,diff,multiply,simplesum,simplediff,simplemult,repeat,sort,wish,wewish
functions=[add,diff,multiply,simplesum,simplediff,simplemult,repeat,sort,wish,wewish]
functiondir=list(functions)
def addclient(identitynum):
	if len(functions)>0:
		try:
			con=lite.connect("client.db")
			with con:
				cur=con.cursor()
				functemp=random.choice(functions)
				ind=functions.index(functemp)
				#cur.execute("INSERT INTO Clients(identity,functionnum) VALUES (identity,ind)")
				query="INSERT INTO Clients(identity,functionnum) VALUES (?,?)"
				data=(identitynum,ind)
				cur.execute(query,data)
				print(f"Function num is {ind}")
				con.commit()
				functions.pop(ind)
				return 1,ind
		except:
			print("Client already exists")
	return 0,0

def checkresponse(client,key,response):
	con=lite.connect("client.db")
	with con:
		cur=con.cursor()
		query='''SELECT functionnum FROM Clients WHERE identity=?'''
		cur.execute(query,(client,))
		ans=cur.fetchall()
		if len(ans)>0:
			expectedans=functiondir[ans[0][0]](key)
			print(expectedans)
			print(f"Function is {functiondir[ans[0][0]]}")
			if expectedans==response:
				return 1
	return 0
