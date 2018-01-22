#!/usr/bin/env python
from scapy.all import *

ipaddr = []
macaddr = []

def findARP(p):
  if p.haslayer(ARP):
      n = len(ipaddr)     	      # number of known hosts

      known = 0
      for i in range(n):
        if p.psrc == ipaddr[i]:     # packet announces a known host
          known = 1
          if p.hwsrc != macaddr[i]:
            print "ARP Poisoning Detected!"
            print ipaddr[i], " was at ", macaddr[i], "moved to ", p.hwsrc
      if known == 0:
        ipaddr.append(p.psrc)
        macaddr.append(p.hwsrc)
        print "New host announced", ipaddr, macaddr

sniff(prn=findARP)



