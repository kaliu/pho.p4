import os, sys

buf = raw_input();

if len(buf) < 10:
	for i in range (len(buf), 10):
		buf += '\x00'
	buf += 'A+'

elif len(buf) > 10:
	buf = buf[:-(len(buf) - 10)]
	#buf += '\x00\x00'
	buf += 'A+'

print buf

