#Headers
from ctypes import * 
import socket        
import struct        
import os
import sys
import signal
import select


PROTO_MAP = {
        1 : "ICMP",
        6 : "TCP",
        17: "UDP",}




class IP(Structure):
    _fields_ = [("ip_hl" , c_ubyte, 4), 
                ("ip_v"  , c_ubyte, 4), 
                ("ip_tos", c_ubyte),    
                ("ip_len", c_ushort),   
                ("ip_id" , c_ushort),   
                ("ip_off", c_ushort),   
                ("ip_ttl", c_ubyte),      #structure of my
                ("ip_p"  , c_ubyte),    
                ("ip_sum", c_ushort),   
                ("ip_src", c_uint32),
                ("ip_dst", c_uint32)]   

    def __new__(self, buf=None):
        return self.from_buffer_copy(buf)
    
    def __init__(self, buf=None):
        
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.ip_src))
        self.dst_address=socket.inet_ntoa(struct.pack("@I",self.ip_dst))
        


        try:
            self.proto = PROTO_MAP[self.ip_p]
        except KeyError:
            print("{} Not in map".format(self.ip_p))
            



host = ''
s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#s.bind((host, 0))

print("Sniffer started...")
try:
    while True:
        buf = s.recvfrom(65535)[0]
        ip_header = IP(buf[:20])
        print("soures Ip : " +ip_header.dst_address + " | Protocal :" + ip_header.proto +" | destination ip : "+ ip_header.src_address)
except KeyboardInterrupt:
    s.close()
