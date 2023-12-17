from random import shuffle, seed, randint as ri
from Crypto.Util.number import bytes_to_long

def encrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext

flag = "shellmates{redacted}"
assert len(flag)%12==0
mykey = bytearray([ri(0, 255) for _ in range(12)])
print(mykey)
pt = flag[11:-1]
print(pt)
l_pt = list(pt)
seed(bytes_to_long(mykey))
shuffle(l_pt)
shuffled_flag = "shellmates{" + "".join(l_pt) + "}"
enc = encrypt(shuffled_flag.encode(), mykey)
print(enc)

# enc = b'S64\xd1\xeeG\x95\xcf\rl\xe3n\x7f\x013\xd3\xf4M\x80\xff<@\xcd\x18h\te\xe2\xa3d\xad\x9f\r/\xf6X\x7f\x0cb\xcf\xe3O\x8d\xd2\x00J\xd9\x18W\x15b\xe2\xc0d\xbd\xde7V\xebn\x7f\x1d\x1f\xe2\xc6G\xc4\xe4-s\xc7V'