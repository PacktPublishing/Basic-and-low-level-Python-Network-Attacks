#!/usr/bin/env python
from scapy.all import *

ipsrc = []
domain = []

def findRA(p):
  if p.haslayer(ICMPv6NDOptPrefixInfo):
    print p[ICMPv6NDOptPrefixInfo].summary()

sniff(prn=findRA)
