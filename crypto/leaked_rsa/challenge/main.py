from Crypto.Util.number import *
from secret import flag

p = getPrime(512)
q = getPrime(512)

e = 65537

while p<q:
    q=getPrime(512)

n = p*q

eq = (n**3)*(5*(p+1)**2 + pow(p,4)) + 5*n*(q+p) + q**2

flag_num = bytes_to_long(flag)

c = pow(flag_num, e, n)

with open('output.txt', 'w') as f:
    f.write(f"{n =}\n{c =}\n{e =}\n{eq =}")
