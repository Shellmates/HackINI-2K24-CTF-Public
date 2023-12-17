import base64
import random

FLAG = "shellmates{YooU_H4v3_7O_KNOW_B4s364_Ch4r4c73R2}"

encoded = base64.b64encode(FLAG.encode())


b64_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
all_bytes = set(chr(i) for i in range(256))
non_b64_chars = list(all_bytes - b64_chars)
boosed = b""

for i in range(len(encoded)):
    boosed += encoded[i].to_bytes(1, "big")
    x = random.randint(0, 3)
    for i in range(x):
        boosed += random.choice(non_b64_chars).encode()

         
open("../FLAG.B1337", "wb").write(boosed)