#!/usr/bin/env python
import sys, time
from scapy.all import *

conf.L3socket
conf.L3socket=L3RawSocket

i=IP()
i.dst="packtpub.samsclass.info"

t = TCP()
t.sport=2009
t.dport=40001

r = sr1(i/t, timeout = 2)

t.flags="A"
t.seq = r.ack
t.ack = r.seq + 1

send(i/t/"SAMTEST4")


