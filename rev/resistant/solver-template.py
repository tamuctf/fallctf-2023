from pwn import *

context.log_level = "debug"
io = remote("ctf.cybr.club", 443, ssl=True, sni="resistant")
io.recvall()
