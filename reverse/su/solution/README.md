# Challenge name

## Write-up


You can find this constraint with static (Ghidra) and dynamic analysis (GDB):
```
"(password[0] == 36)",
"(password[1] == 85)",
"(password[2] == 80)",
"(password[3]==51)",
"(password[4]==82)",
"(password[5]==95)",
"(password[6]==36)",
"(password[7]==51)",
"(password[8]==67)",
"(password[9]==82)",
"(password[10]==51)",
"(password[11]==84)",
"(password[12]==95)",
"((password[13] & 0x1fffffff) == 0x6b)",
"(password[14]>>2 == 12)",
"(password[15]== 89)"
```
Write a script then you will find the password `$UP3R_$3CR3T_k3Y` . 
## flag

`shellmates{$UP3R_$3CR3T_k3Y}`
