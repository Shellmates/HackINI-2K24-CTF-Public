#!/bin/python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

flag = open('flag', 'rb').read()+b'Free Palestine.'

def aes_enc(key, pt):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.encrypt(pt)

pt = pad(flag, AES.block_size)

pt = [pt[i:i + AES.block_size] for i in range(0, len(pt), AES.block_size)]

ct = pt.copy()

for i in range(len(pt)):
    ct[i] = aes_enc(ct[i-1],pt[i])

open('enc','wb').write(b''.join(ct))
