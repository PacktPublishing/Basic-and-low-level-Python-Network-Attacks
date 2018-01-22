import socket
s = socket.socket()

s.connect(("packtpub.samsclass.info", 23))
print s.recv(1024)
s.close()


