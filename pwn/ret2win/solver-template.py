from pwn import *

context.log_level = "debug"
io = remote("tamuctf.com", 443, ssl=True, sni="ret2win")
io.interactive(prompt="")
