#!/usr/bin/python2
import random
import os
import sys

def generate_random_key(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))

def encrypt(plain_string, key):
    encrypted = []
    for i in range(len(plain_string)):
        encrypted_char = (ord(plain_string[i]) * ord(key[i % len(key)]) + pow(i,16))
        encrypted.append(encrypted_char)
    return encrypted

def check_input(input_str, passphrase):
    if input_str == passphrase:
        print("Well Done Reverser.")
        return True
    else:
        print("Try again.")
        return False

if __name__ == "__main__":
    PASSPHRASE = os.getenv('PASSPHRASE')
    key = generate_random_key(10)
    print("Encryption Key: "+key+"\n")
    print("Encrypted Passphrase: \n")
    #sys.stdout.flush()
    print(encrypt(PASSPHRASE,key))
    print("Enter the decrypted passphrase: ")
    sys.stdout.flush()
    user_input = raw_input()
    if check_input(user_input, PASSPHRASE):
        FLAG = open('flag.txt', 'r').read()
        print(FLAG)
