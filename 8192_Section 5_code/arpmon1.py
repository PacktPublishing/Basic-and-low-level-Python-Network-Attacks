#!/usr/bin/env python
from scapy.all import *

def findARP(p):
  if p.haslayer(ARP):
    print p.summary()
    print p.display()

sniff(prn=findARP)

