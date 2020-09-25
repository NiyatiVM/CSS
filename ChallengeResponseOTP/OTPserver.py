import socket
import random
from functionlibrary import add,diff,multiply,simplesum,simplediff,simplemult,repeat,sort,wish,wewish
from serverdb import addclient,checkresponse
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation has some errors %s"%err)

port=1999

s.bind(('',port))
print("Socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")

while True:
	c,addr =s.accept()
	print("Got connection from",addr)
	identity=c.recv(1024).decode()
	identity=int(identity)
	print(f"The id of client is {identity}")
	c.send("1.Add 2.Authenticate:\n".encode())
	mode=int(c.recv(1024).decode())
	if mode==1:
		process=addclient(identity)
		if process[0]==1:
			c.send("1".encode())
			c.send("Successfully added as a client".encode())
			c.send(str(process[1]).encode())
		else:
			c.send("0".encode())
			c.send("You are an existing client or maximum clients already exist".encode())
	else:
		key=random.randint(10,5000)
		c.send(str(key).encode())
		response=int(c.recv(1024).decode())
		auth=checkresponse(identity,key,response)
		if auth:
			c.send("1".encode())
			print("It's a Match!")
			c.send("Successfully Authenticated !!".encode())
			c.send("Finally we can share our messages".encode())
		else:
			c.send("0".encode())
			print("Register first")
			c.send("Not authenticated".encode())
		c.send("Thank you for connecting".encode())
	c.close()