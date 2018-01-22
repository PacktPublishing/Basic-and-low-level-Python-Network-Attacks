import socket
s = socket.socket()
s.settimeout(2)
t = socket.socket()

try:
	s.connect(("packtpub.samsclass.info", 20000))
	r = s.recv(1024)
        print r
        port2 = int(r[24:29])

        print "Connecting to port", port2
	t.connect(("packtpub.samsclass.info", port2))
	print t.recv(1024)

	s.close()
except socket.error as err:
	print err



