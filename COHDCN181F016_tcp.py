from ctypes import *
import sys
import socket
import struct
import os

class TCP_class(Structure):
    _fields_=[
        ("Source", c_ushort), # Foreign Function Library
        ("destination", c_ushort), #Represent unsigned short data type 
        ("sequence_no", c_long), #signed long
        ("acknowledge_no", c_long),
        ("Offset", c_ubyte, 4), #Represent  Unsigned char , interprets the vlue as samall int
        ("Reserved", c_ubyte, 4),
        ("Flag",  c_ubyte),
        ("Window", c_ushort),
        ("CheckSum", c_ushort),
        ("URG_point", c_ushort), #Represent Unsigned Short
        ]
