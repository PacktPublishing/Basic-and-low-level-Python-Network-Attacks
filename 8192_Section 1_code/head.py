import socket
s = socket.socket()
s.settimeout(2)

target = 'packtpub.samsclass.info'
s.connect((target, 80))

req = 'HEAD / HTTP/1.1\r\nHost: ' + target + '\r\n\r\n'
print 'Sending: '
print req
s.send(req)

print 'Received: '
print s.recv(1024)

s.close()
