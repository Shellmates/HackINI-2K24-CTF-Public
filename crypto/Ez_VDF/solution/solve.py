from pwn import *

# r = process(['python','chall.py'])
r = remote('localhost', 8000)
N = int(r.recvline().decode().split('=')[1])
gen = int(r.recvline().decode().split(':')[1])
mygen = (gen**2)%N
r.recvuntil(b':')
r.sendline(f"{mygen}".encode())
r.recvline()
proof = int(r.recvline().decode().split(':')[1])
r.sendline(f"{proof**2%N}".encode())
r.interactive()