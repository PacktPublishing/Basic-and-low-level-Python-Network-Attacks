#!/usr/bin/env python
from scapy.all import *

ipsrc = []
domain = []

def findTCP(p):
  if p.haslayer(TCP):
    print p[IP].src, p[IP].dst
    flags = p.sprintf("%TCP.flags%")
    if flags == "S":   
      print "flag", flags

sniff(prn=findTCP)
