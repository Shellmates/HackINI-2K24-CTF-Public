from pwn import xor
ct = b'\x1c62\x8f|i\x9a\xadw\xba\x06N\x85\x08+d\xb0C[\xa9\xed|\x8dM\x12\xb4\\\r$\xbct4\x9e\xaaM\x872\x0b\x85.\x12\x00\xa2iW\xa4\xb4W\xfd3 \xa3\x00\x0b\x08\xb1O \x9e\x9ag\xbbN^\xa7'
def encrypt(plaintext, key):
    ciphertext = bytearray([plaintext[i] ^ key[i%len(key)] for i in range(len(plaintext))])
    return ciphertext
otp1 = b"shellmates{"
first_part = encrypt(ct, otp1)[:11]
otp2 = b"}"
last_part = xor(otp2, ct[-1])
for i in range(256):
    b = bytes(first_part)+bytes([i])+bytes(last_part)
    print(encrypt(ct, b))