import socket

for port in range(3000, 4000, 100):
   try:
	s = socket.socket()
	s.settimeout(2)
	print "Trying port ", port
	s.connect(("packtpub.samsclass.info", port))
	print s.recv(1024)
	s.close()
   except socket.error as err:
	print err



