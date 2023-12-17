# Analayzing the binary
- A golang binary is given
```bash
>>> file app
app: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=TknC1-1nBMzMTBUXDr_1/QuJ09WuiC_9MVmkYh2yo/FPqOCh5lUlXPycbD348F/dnbrs02rskrlanoHo8QX, not stripped
```
- The binary is not stripped which means the debugging will be easier using symbols
- Let's try to run it
```
Welcome to our JOKES store, we'll be glad to serve you

How can we serve you?
1. Hear a joke
2. Suggest a joke
3. Hear a special joke
4. Leave
```
- Choosing the first choice will display a joke for us
- Choosing the second one will give us the ability to write a joke
- Choosing the third one will ask us for a VIP ticket so we can guess that's the right path to find the flag
- Let's open it in `Ida` and go to the main function
```go
  while ( (unsigned __int64)&retaddr <= *(_QWORD *)(v0 + 16) )
    runtime_morestack_noctxt();
  v6[0] = &RTYPE_string;
  v6[1] = &off_4F87C0;
  v1 = fmt_Fprintln(&off_4F8D98, qword_594650, v6, 1LL, 1LL);

  for ( i = main_Menu(v1); i > 2; i = main_Menu(v3) ) {
    if ( i == 3 ) {
      v3 = main_HearSpecialJoke();
    } else {
      if ( i != 4 )
        goto LABEL_11;
      v5[0] = &RTYPE_string;
      v5[1] = &off_4F87D0;
      fmt_Fprintln(&off_4F8D98, qword_594650, v5, 1LL, 1LL);
      v3 = os_Exit(0LL);
    }
LABEL_3:
    ;
  }
  if ( i == 1 ) {
    v3 = main_HearJoke();
    goto LABEL_3;
  }
  if ( i == 2 ) {
    v3 = main_SuggestJoke();
    goto LABEL_3;
  }
LABEL_11:
  v4[0] = &RTYPE_string;
  v4[1] = &off_4F87E0;
  v3 = fmt_Fprintln(&off_4F8D98, qword_594650, v4, 1LL, 1LL);
  goto LABEL_3;
}
```
- We can guess that there's a function `main_Menu` that returns the choice number on which is based the next function call
- By using a debugger an breaking after the call of `main_Menu` we can see that it returns the choice we entered so we can confirm our previous guess
- What interests us is the function `main_HearSpecialJoke`
```go
  MustCompile = regexp_MustCompile(
                  (__int64)"^[0-9A-Z]{4}-[0-9A-Z]{4}-[0-9A-Z]{4}-[0-9A-Z]{4}$",
                  49LL,
                  a3,
                  a4,
                  a5,
                  a6,
                  a7,
                  a8,
                  a9);
```
- It starts by an init to `regex_MustCompile` which can be used in golang to verify string patters so we can say that's the format of the VIP ticket
```go
if ( regexp__ptr_Regexp_doExecute(0LL, 0LL, v22, 0LL, 0LL, v32) )
```
- By following the ticket using a debugger we'll find it's passed as an argument to another function `main_CheckTicketValidity`
```go
if ( (unsigned __int8)main_CheckTicketValidity(v32, v31) )
```
- In `main_CheckTicketValidity` we can see that it's spliting the input to an array using `strings_genSplit` with `-` as a value of `&unk_4F77F8` which is the separator
```go
v10 = (_QWORD *)strings_genSplit(a1, a2, (unsigned int)&unk_4F77F8, 1, 0, -1, a7, a8, a9);
```
- Analayzing the rest give us an idea that there's a loop where a function `main_CheckHash` is called in each iteration
```go
while ( a2 > v15 ) {
  v21 = v15;
  v22 = v10;
  if ( !(unsigned __int8)main_CheckHash(*v10, v10[1], v15, 1, 0, v11, v12, v13, v14, v17, v18, v19) )
    return 0LL;
  v10 = v22 + 2;
  v15 = v21 + 1;
  a2 = v20;
}
```
- By using a debugger and following each iteration it seems that it passes in each iteration on of the strings resulted 
- Following the function `main_CheckHash` using GDB we see that it generates the MD5 hash of each part of the ticket
- Then it compares it with a hash stored in a global variable nammed `HASHS`
- Using a decompiler like `Ghidra` will be useful in this case to retrieve the values of `HASHS` or we can directly get them using `GDB` by breaking and following the registers after the generation of the hash of the ticket part
```py
HASHS = [
    "efbef50a500a775721a668f0fde8ebfd",
    "28c31a8b4b0a54bf02cdcb08a2cc9d68",
    "1fecc0f2d559d5f440da1820d5399fb2",
    "87ecd4873b986300b07e1d4eff6d95e5"
]
```
- By analzying the rest in Ida and following the registers in GDB we'll find that it's doing a comparaison between the result hash and the existing hash
```go
 if ( main_HASHS[2 * v44 + 1] == v30 )
    return runtime_memequal(v31, main_HASHS[2 * v44], v30);
```
- If the hashs are not equal it returns and displays `Invalid VIP ticket`
- If `main_CheckTicketValidity` returns `true` an environement variable with the key `FLAG` is loaded and displayed which is the goal
```go
if ( github_com_joho_godotenv_Load(0, 0, 0, 0, 0, v37, v38, v39, v40, error_codea, error_code_8a, v103) )
```
```go
v108 = os_Getenv((unsigned int)"FLAG", 4, v41, v30, v31, v42, v43, v44, v45, error_codeb, error_code_8b);

```

# Solution
- So basicly we have to find the correct VIP ticket that will be splitted into four parts that verifies the previous hashs
- Cracking it will be the only solution in this case, seeing the range from the previous regex `[0-9A-Z]{4}` there's `1679616` possibility which a small number to crack
- The operation four times to crack the hash of each part, once we get the four parts we'll have the VIP ticket

# Solve script
```py
from hashlib import md5

def calculate_md5(data):
    md5_hash = md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

HASHS = [
    "efbef50a500a775721a668f0fde8ebfd",
    "28c31a8b4b0a54bf02cdcb08a2cc9d68",
    "1fecc0f2d559d5f440da1820d5399fb2",
    "87ecd4873b986300b07e1d4eff6d95e5"
]

parts = []

for p in HASHS:
    for i in range(36):
        for j in range(36):
            for k in range(36):
                for l in range(36):
                    data = chars[i] + chars[j] + chars[k] + chars[l]
                    if calculate_md5(data) == p:
                        parts.append(data)
                        break

print("-".join(parts))
```

# Flag
> shellmates{w3Lc0m3_t0_tH3_w0rLD_0f_g0L4nG}