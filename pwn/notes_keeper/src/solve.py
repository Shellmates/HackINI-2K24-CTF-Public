#!/usr/bin/env python3
from pwn import *
import ctypes
from time import sleep

exe=ELF("./chal")

HOST, PORT = "",7777

context.binary = exe

# Constants

GDBSCRIPT = '''\
'''
CHECKING = True


def create(title, content):
    io.sendline(b"1")
    io.recv()
    io.sendline(title)
    io.recv()
    io.sendline(content)
    io.recv()

def delete(index):
    io.sendline(b"2")
    io.recv()
    io.sendline(str(index).encode())
    io.recv()

def view(index):
    io.sendline(b"3")
    io.recv()
    io.sendline(str(index).encode())
    io.recv()

def edit(title, content):
    io.sendline(b"4")
    io.recv()
    io.sendline(title)
    io.recv()
    io.sendline(content)
    io.recv()

def main():
    global io
    io = conn()
    io.interactive()

    
    
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
        p = gdb.debug(exe.path, gdbscript=GDBSCRIPT,aslr=False)
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





