# diffie_3ilman

## Write-up
- We want to provide a k such as the shared key could be known after that like shared_key=1.
- We observe that using k=1 or k=p-1 is prohibited...
- So we'll try another approach it's k=(p-1)//2 because (p-1)%2=0 always, we'll think for quadratic residue legendre symbol
- if B is quadratic residue it B^k mod p = 1. 
- with this input we'll have the shared key is 1 and it's simple to decrypt it using AES
## Flag

`shellmates{D0_n0t_L3t_Str4ngers_Pl4y_w1th_D1ffie_H3llman_p4ram$}`
