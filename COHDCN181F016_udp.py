from ctypes import *
import struct
import socket
import sys
import os


class UDP_class(Structure):
    _fields_=[
        ("Source", c_ushort),
        ("Destination", c_ushort),
        ("Length", c_short),
        ("CheckSUM", c_short),
        ]
