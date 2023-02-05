#!/usr/bin/Python3

from scapy.all import *

ID = 1000
dst_ip = "10.0.2.8" #srver's IP address

#Fragment no.1
udp = UDP(sport=7070, dport=9090, chksum=0)
udp.len = 8 + 32 + 40 + 20

ip = IP(dst=dst_ip, id=ID, frag=0, flags=1)
payload = "A" * 31 + "\n"
pkt = ip/udp/payload
send(pkt, verbose=0)

#Fragment No.2
ip = IP(dst=dst_ip, id=ID, frag=5, flags=1)
ip.proto = 17
payload = "B" * 39 + "\n"
pkt = ip/payload
send(pkt, verbose=0)

#Fragment No.3
ip = IP(dst=dst_ip, id=ID, frag=11, flags=0)
ip.proto = 17
payload = "C" * 19 + "\n"
pkt = ip/payload
send(pkt, verbose=0)

