# Beginner Hacker 1

## Write-up

### Solution Steps:
1. Understanding the Constraint:
As we can clearly see the key lenghth is 12 bytes and len(flag)%12==0 and the encryption is just a simple xor between the flag and the key.

2.  XOR Encryption Overview:
XOR encryption involves bitwise XOR operation between corresponding bits of the plaintext and the key. In this challenge, the task is to recover the key to get the flag since one key is used for both encryptions.

3. Approach:
the known values are 'shellmates{' and '}' so we can recover the first 11 bytes of the key, but can we recover a byte using the the prefix '}' ?
Yes, we can do that since len(flag)%12==0 and len(key)==12.
As we can see the flag content is shuffled using a seed which is the key, so after recovering the key we can use it to unshuffle the flag content, for this task we can use the unshuffle function that i used in solution.py or use another one online.
## Flag

`shellmates{ev3n_D0Uble_EnCRYti0N_Is_B4D_WHeN_wE_ar3_UsINg_ThE_$Am3_K3y!}`
