import socket
s = socket.socket()
s.bind(("localhost",8888))
s.listen(4)
print('Server is ready for get input form Client')

while (True):
    cs,ca = s.accept()
    csmsg = cs.recv(2048).decode()
    print("Student:\t{}".format(csmsg))
    sendmsg = input("Teacher:\t")
    cs.send(sendmsg.encode())