from Crypto.Util.number import bytes_to_long , getPrime 
import random


FLAG="shellmates{FakeFlag}"

FLAG=FLAG.lstrip('shellmates{').rstrip('}')
cipher = []
mod = []
plain = bytes_to_long(FLAG.encode())    


Q = getPrime(128)
P = getPrime(128)
N = P*Q
e = getPrime(32)


d = pow(e,-1,(P-1)*(Q-1))
enc = pow(plain,e,N )


k=random.randint(1,32)
print(k)
old_e = bin(e)[2:]
new_e=old_e[0:k]+old_e[k+2:]

print(len(old_e),len(new_e))

print(f"{N=}")
print(f"e={int(new_e,2)}")
print(f"{P=}")
print(f"{Q=}")

ec = 71
print(f"{ec=}")    
for i in range(10) : 
    q = getPrime(1024)
    p = getPrime(1024)
    assert p != q
    n = p*q 
    c = pow(enc , ec ,n )
    mod.append(n)
    cipher.append(c)
    assert ( pow(plain,ec)  > n)  
      


print(f"{cipher=}")
print(f"{mod=}")
