#!/usr/bin/env python
from scapy.all import *
from random import randint

# Use the lowest number after several traceroutes
numhops = 11

conf.L3socket
conf.L3socket=L3RawSocket

i=IP()
i.dst="packtpub.samsclass.info"

msg = raw_input("Name: ")

win = 0
attempt = 0

while (win < 10) and (attempt < 10):
  sport = randint(0, 9999)
  for j in range(13,14):
    i.ttl = 64
    t = TCP()
    t.dport=40002
    t.sport=sport + j
    r = sr1(i/t, timeout=2)
    attempt += 1

    try:
      flags = r.sprintf("%TCP.flags%")
      if flags == "SA":
        print "SYN/ACK Received", r.summary()
        t.flags="A"
        t.seq = r.ack
        t.ack = r.seq + 1

        i.ttl = numhops
        send(i/t/msg)

        i.ttl = numhops+1
        send(i/t/msg)

        i.ttl = numhops+2
        send(i/t/msg)

        i.ttl = numhops+3
        send(i/t/msg)

        win += 1
      else:
        print "TCP reply, but not a SYN/ACK", r.summary()
    except:
      try:
         print "Non-TCP Reply", r.summary()
      except:
         print "No Reply"


