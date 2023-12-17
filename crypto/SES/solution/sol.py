from Crypto.Cipher import AES

def aes_dec(key, ct):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.decrypt(ct)

ct = open('enc', 'rb').read()
ct = [ ct[i:i+16] for i in range(0, len(ct),16) ]

fact = b'Free Palestine.'

for i in range(1,0x11):
    key = fact[i-1:]+i.to_bytes()*i
    if b'shellmates' in aes_dec(key, ct[0]):
        pt = ct.copy()
        pt[-1] = key
        for j in reversed(range(len(ct))):
            pt[j] = aes_dec(pt[j-1], ct[j])
        break
print(b''.join(pt))
