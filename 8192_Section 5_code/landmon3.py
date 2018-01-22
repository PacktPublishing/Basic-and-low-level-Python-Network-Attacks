#!/usr/bin/env python
from scapy.all import *

def findTCP(p):
  if p.haslayer(TCP):
    if p[IP].src == p[IP].dst:
      flags = p.sprintf("%TCP.flags%")
      if flags == "S":   
        print "Land attack detected!"
        print p.summary()

sniff(prn=findTCP)
