# Beginner Hacker 1

## Write-up

### Solution Steps:
1. Understanding the Constraint:
As we can clearly see the key lenghth is 13 bytes and len(flag)%13==0 and the encryption is just a simple xor between the flag and the key.

2.  XOR Encryption Overview:
XOR encryption involves bitwise XOR operation between corresponding bits of the plaintext and the key. In this challenge, the task is to recover the key to get the flag.

3. Approach:
the known values are 'shellmates{' and '}' so we can recover the first 11 bytes of the key, but can we recover a byte using the the prefix '}' ?
Yes, we can do that since len(flag)%13==0 and len(key)==13.
We are know one byte short to get the flag, we can recover it using brute force since there is only 256 possibilities for that one byte.
## Flag

`shellmates{1_gu3SS_R4nD0mn3Ss_d0es_NOt_ALWAyS_mE4N_yoU_R_$eCur3!}`
