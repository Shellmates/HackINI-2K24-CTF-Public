import os
try:
    a = float(input('a = '))
    if a == a:
        print('No No No ...')
    else:
        flag = open('flag.txt', 'r').read()
        print(flag)
except:
    print('No No No ...')