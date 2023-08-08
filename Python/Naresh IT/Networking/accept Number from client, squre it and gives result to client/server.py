import socket
s = socket.socket()
s.bind(("localhost",8888))
s.listen(2)
print('Server is ready for get input form Client')

while True:
    try:
        cs,ca = s.accept()
        csval = cs.recv(1024).decode()
        print("Val of client = {}".format(csval))
        res = int(csval)**2
        cs.send(str(res).encode())
    except ValueError:
        print("Connection failed")
