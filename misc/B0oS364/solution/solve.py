import base64
import random

b64_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
all_bytes = set(chr(i) for i in range(256))
non_b64_chars = list(all_bytes - b64_chars)

boosed = open("FLAG.B1337", "rb").read()

flag = b""
for i in range(len(boosed)):
    if boosed[i] not in non_b64_chars:
        flag += boosed[i].to_bytes(1, "big")
print(base64.b64decode(flag).decode())