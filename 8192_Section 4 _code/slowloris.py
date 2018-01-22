#!/usr/bin/env python
from scapy.all import *

conf.L3socket
conf.L3socket = L3RawSocket

i = IP()
i.dst = "172.16.1.188"


req = "GET / HTTP/1.1\r\nHost: 172.16.1.188"

for p in range(2000,2010):
  t = TCP()
  t.dport = 80
  t.sport = p
  r = sr1(i/t)

  t.flags = "A"
  t.seq = r.ack
  t.ack = r.seq + 1
  send(i/t/req)





