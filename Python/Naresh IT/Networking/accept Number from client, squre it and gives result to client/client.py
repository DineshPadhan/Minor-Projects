import socket
s = socket.socket()
s.connect(("localhost",8888))
print("Client is connected to server")
print("-"*50)
n = input("Enter The number: ")
s.send(n.encode())

res = s.recv(1024).decode()
print("Sqr({}) = {}".format(n,res))