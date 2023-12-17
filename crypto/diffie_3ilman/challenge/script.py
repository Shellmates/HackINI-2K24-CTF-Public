from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
from random import randint
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


with open("flag.txt", "rb") as f:
    flag = f.read().strip()

def main():
    print("I know that diffie hellman is robust so I let you play with parameters")

    g, p = 2, getPrime(1024)
    a = randint(2, p - 1)
    A = pow(g, a, p)
    print("Public key:")
    print(f"{g = }")
    print(f"{p = }")
    print(f"{A = }")

    try:
        k = int(input("Choose k = "))
    except:
        print("please enter a number...")
        return
    if k == 1 or k == p - 1 or k <= 0 or k >= p:
        print("Noooo not like that...")
        return

    Ak = pow(A, k, p)
    b = randint(2, p - 1)
    B = pow(g, b, p)
    Bk = pow(B, k, p)
    shared = pow(Bk, a, p)

    key = hashlib.md5(long_to_bytes(shared)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    c = bytes_to_long(cipher.encrypt(pad(flag, 16)))

    print("chipherText: ")
    print(f"    {c = }")
    return

if __name__ == "__main__":
    main()