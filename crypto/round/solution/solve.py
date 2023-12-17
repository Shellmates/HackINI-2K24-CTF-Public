from aeskeyschedule import reverse_key_schedule
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify as u

enc = '8fbabbaca2683abbb15d1340a7f79b4d5f26b687364f3af7e71809ee99fbd52b6875fa776b4a4624f775bc6d4f6d904a'
round_key = '8be4f2ecfb5522a1adfbdebd0be57d8d'


for i in range(10):
    key = reverse_key_schedule(u(round_key), i)
    aes = AES.new(key, AES.MODE_ECB)

    flag = aes.decrypt(u(enc))

    if b'shellmates' in flag:
        print(f'it was the {i}th round.')
        print(unpad(flag,16))
        break