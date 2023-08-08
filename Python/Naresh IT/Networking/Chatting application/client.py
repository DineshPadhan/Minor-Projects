import socket
s = socket.socket()
s.connect(("localhost",8888))
print("Client is connected to server")
while (True):
    cspmsg = input("Student:\t")
    s.send(cspmsg.encode())
    if cspmsg.lower() =="bye":
        break
    else:
        sermsg = s.recv(2048).decode()
        print("Teacher:\t{}".format(sermsg))