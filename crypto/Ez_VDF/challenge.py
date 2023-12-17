#!/usr/local/bin/python3

from Crypto.Util.number import getPrime, getRandomInteger

FLAG = 'shellmates{REDACTED}'
P=getPrime(1024)
Q=getPrime(1024)
N=P*Q
print(f'{N=}')

generator=getRandomInteger(512)
print(f'My generator: {generator}')
try:
    usergenerator = int(input('Give me your generator : '))
except:
    print('Give me a valid number')
    exit()

if usergenerator>2 and usergenerator<N-1 and usergenerator!=generator and (-usergenerator)%N != generator:
    print('Valid generator')
else:
    print('HEHE, What are you trying to do?')
    exit()

proof=pow(generator,pow(2,2**256,(P-1)*(Q-1)),N) # g**(2**(2**256)) % N

print(f'The proof is : {proof}')

try:
    userproof = int(input('Give me your proof : ')) 
except:
    print('Give me a valid number')
    exit()

if (pow(usergenerator,pow(2,2**256,(P-1)*(Q-1)),N) == userproof):
    print(f"Here's your flag: {FLAG}")
    exit()


print('Better luck next time')
