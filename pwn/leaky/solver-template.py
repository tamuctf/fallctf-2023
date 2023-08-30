from pwn import *

context.log_level = "debug"
io = remote("example.com", 443, ssl=True, sni="leaky")
io.recvall()
