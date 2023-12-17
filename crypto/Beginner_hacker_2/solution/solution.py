from pwn import xor
import random
from Crypto.Util.number import bytes_to_long

# bytearray(b' ^Q\xbd\x82*\xf4\xbbh\x1f\x98+')

def getperm(l, seed):
    random.seed(seed)
    perm = list(range(len(l)))
    random.shuffle(perm)
    # random.seed()  # optional, in order to not impact other code based on random
    return perm

def unshuffle(l, seed):  
    perm = getperm(l, seed)  
    res = [None] * len(l)  
    for i, j in enumerate(perm):
        res[j] = l[i]
    l[:] = res  

ct = b'S64\xd1\xeeG\x95\xcf\rl\xe3n\x7f\x013\xd3\xf4M\x80\xff<@\xcd\x18h\te\xe2\xa3d\xad\x9f\r/\xf6X\x7f\x0cb\xcf\xe3O\x8d\xd2\x00J\xd9\x18W\x15b\xe2\xc0d\xbd\xde7V\xebn\x7f\x1d\x1f\xe2\xc6G\xc4\xe4-s\xc7V'
def encrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext
otp1 = b"shellmates{"
first_part = encrypt(ct, otp1)[:11]
otp2 = b"}"
last_part = xor(otp2, ct[-1])
mykey = first_part+last_part
my_seed = bytes_to_long(mykey)
shuffled_flag = encrypt(ct, mykey)
ct = list(shuffled_flag[11:-1])
unshuffle(ct, my_seed)
print("shellmates{", end="")
for c in ct:print(chr(c), end="")
print("}")