#!/usr/bin/env python
from scapy.all import *

conf.L3socket
conf.L3socket=L3RawSocket

i=IP()
i.dst = "packtpub.samsclass.info"

t = TCP()
t.dport = 80

r = sr1(i/t)

t.flags="A"
t.seq = r.ack
t.ack = r.seq + 1

req = "GET / HTTP/1.1\r\n" + \
  "Host: packtpub.samsclass.info\r\n\r\n"
send(i/t/req)

reply = sniff(4)
wireshark(reply)


