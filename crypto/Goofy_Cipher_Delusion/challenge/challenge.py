from Crypto.Util.number import getPrime , bytes_to_long
from secret import FLAG

P = getPrime(1024)
Q = getPrime(1024)
e=131
N=P*Q

c=pow(bytes_to_long(FLAG),e,N)
cp=pow(bytes_to_long(FLAG),e,P)

assert c>P

with open('out.txt','w') as f:
    f.write(f'{N=}\n')
    f.write(f'{e=}\n')
    f.write(f'{c=}\n')
    f.write(f'{cp=}')


