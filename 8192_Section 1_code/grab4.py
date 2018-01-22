import socket
s = socket.socket()
s.settimeout(2)

port = raw_input("Port number: ")
try:
	s.connect(("packtpub.samsclass.info", int(port)))
	print s.recv(1024)
	s.close()
except socket.error as err:
	print err




