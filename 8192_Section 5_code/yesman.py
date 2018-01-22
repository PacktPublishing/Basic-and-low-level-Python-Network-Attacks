#!/usr/bin/env python
import sys
from scapy.all import *

def findSYN(p):
    flags = p.sprintf("%TCP.flags%")
    if flags == "S":        # Only respond to SYN Packets
            ip = p[IP]      # Received IP Packet
            tcp = p[TCP]    # Received TCP Segment
            i = IP()        # Outgoing IP Packet
            i.dst = ip.src
            i.src = ip.dst
            t = TCP()       # Outgoing TCP Segment
            t.flags = "SA"
            t.dport = tcp.sport
            t.sport = tcp.dport
            t.seq = tcp.ack
            new_ack = tcp.seq + 1
            print "SYN/ACK sent to ",i.dst,":",t.dport
            send(i/t)

sniff(prn=findSYN)
