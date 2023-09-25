from pwn import *

context.log_level = "debug"
io = remote("tamuctf.com", 443, ssl=True, sni="rop2")
io.interactive(prompt="")
