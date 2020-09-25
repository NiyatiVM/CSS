import socket
from functionlibrary import add,diff,multiply,simplesum,simplediff,simplemult,repeat,sort,wish,wewish
from clientdb import adddetails,getdetails
functions=[add,diff,multiply,simplesum,simplediff,simplemult,repeat,sort,wish,wewish]
s=socket.socket()
port=1999
s.connect(('127.0.0.1',port))
identity=int(input("Enter your identity number:\n"))
s.send(str(identity).encode())
print(s.recv(1024).decode())
mode=int(input().strip())
s.send(str(mode).encode())
if mode==1:
	resp=int(s.recv(1024).decode())
	if resp==1:
		print(s.recv(1024).decode())
		clientfunction=int(s.recv(1024).decode())
		print(f"{clientfunction}")
		adddetails(identity,clientfunction)
	else:
		print(s.recv(1024).decode())
elif mode==2:
	key=int(s.recv(1024).decode())
	print(f"The key is:{key}")
	num=getdetails(identity)
	print(f"Function Number is {num}")
	res=functions[num](key)
	print(f"Sending {res}")
	s.send(str(res).encode())
	print(s.recv(1024).decode())
s.close()