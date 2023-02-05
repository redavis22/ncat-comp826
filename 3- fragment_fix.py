#!/usr/bin/Python3

from scapy.all import *

ID = 1000
dst_ip = "10.0.2.8" #srver's IP address

#Missing Piece
ip = IP(dst=dst_ip, id=ID, frag=10, flags=1)
ip.proto = 17
payload = "*" * 8
pkt = ip/payload
send(pkt, verbose=0)



