import socket    
import signal
import struct
from ctypes import *


class IP(Structure):
    _fields_ = [("version",c_ubyte,4),("ihl",c_ubyte,4),("tos",c_ubyte),("lent",c_ushort),("iden",c_ushort),("off",c_ushort),("ttl",c_ubyte),
("proto",c_ubyte),("check",c_ushort),("src",c_uint32),("dst",c_uint32)]

    def __new__(cls,buf=None):
        return cls.from_buffer_copy(buf)
    def __init__(self,buf=None):
        self.src_add=socket.inet_ntoa(struct.pack("@I",self.src))
        self.dst_add=socket.inet_ntoa(struct.pack("@I",self.dst))
        self.Ttl=str(self.ttl)   #Network stream convert to Host

class ICMP(Structure):
    _fields_ = [("types",c_ubyte),("code",c_ubyte),("icmp_check",c_ushort),("icmp_id",c_ushort),("sequ",c_ushort)]

    def __new__(self,buf=None):
        return self.from_buffer_copy(buf)
    def __init__(self,buf=None):
        self.Type=str(self.types)
        self.Code=str(self.code)

def ipPacket():
    dst = input("Enter Ip Address : ")
    src = '192.168.231.129'
    version=4
    tos=0
    lent=60
    iden=1188
    off=0
    ttl=128
    proto=socket.IPPROTO_ICMP
    check=0
    ip_saddr = socket.inet_aton(src)
    ip_daddr = socket.inet_aton(dst)
    ip_pac=struct.pack('!BBHHHBBH4s4s',version,tos,lent,iden,off,ttl,proto,check,ip_saddr,ip_daddr)  #!BBHHHBBH4s4s - c_ubyte /
    return src,dst,ip_pac


def icmpPacket(sock,dst):
    types=8
    code=0
    icmp_check=0
    icmp_id=5656
    sequ=0
    sequ=sequ+1
    payload=0      #ICMP Packet
    icmp_pac=struct.pack('!BBHHHb',types,code,icmp_check,icmp_id,sequ,payload)
    sock.sendto(icmp_pac,(dst,1))
    reply=sock.recv(1024) #Reply
    ip=IP(reply[:20])
    icmp=ICMP(reply[20:28])
    return icmp_pac


sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(3))
(src,dst,ip_pac)=ipPacket()

try:
    while True:
        sock.sendto(ip_pac,(dst,0))
        data=s.recv(1024)
        ip=IP(data[14:])  #First 14 bit - Ethernet Header , ip header
        print ("reply from "+ip.dst_add+ " : bytes=32  "+" TTL :"+ip.Ttl)

except KeyboardInterrupt:
    sock.close()
