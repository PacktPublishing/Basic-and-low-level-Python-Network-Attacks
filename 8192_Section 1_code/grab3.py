import socket
s = socket.socket()
s.settimeout(2)

try:
	s.connect(("packtpub.samsclass.info", 80))
	print s.recv(1024)
	s.close()
except socket.error as err:
	print err



