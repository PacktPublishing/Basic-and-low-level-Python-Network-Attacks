#!/usr/bin/env python
from scapy.all import *

ipsrc = []
domain = []

def findTCP(p):
  if p.haslayer(TCP):
    print p[IP].summary()
    print p[TCP].summary()

sniff(prn=findTCP)
