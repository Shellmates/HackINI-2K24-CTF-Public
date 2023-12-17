from random import randint as ri

def encrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext

flag = b"shellmates{redacted}"
assert len(flag)%13==0
mykey = bytearray([ri(0, 255) for _ in range(13)])  
enc = encrypt(flag, mykey)
print(enc)

# enc = b'\x1c62\x8f|i\x9a\xadw\xba\x06N\x85\x08+d\xb0C[\xa9\xed|\x8dM\x12\xb4\\\r$\xbct4\x9e\xaaM\x872\x0b\x85.\x12\x00\xa2iW\xa4\xb4W\xfd3 \xa3\x00\x0b\x08\xb1O \x9e\x9ag\xbbN^\xa7'