# Analysing the code
- In `__start` section we can find an execution of two `syscall`, by searching on the internet we can specify the system call by specifiying the value of the system call in `RAX`
- The first one is to display `prompt` variable which contains `Enter flag:`
- The second one is reading an input and stores it in `input` variable
```asm
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, prompt_len
    syscall

    mov rax, 0
    mov rdi, 0
    mov rsi, input
    mov rdx, 38
    syscall

    mov rcx, 0
```
- By analzying `check` section we see that it uses `RCX` as an index to verify byte per byte the input and the output which may be the correct flag
- Before verifying it converts the byte to the negative value then it shifts it to the left by 2 bits
```asm
check:
    cmp byte [input + rcx], 10
    je  end

    movzx rax, byte [input + rcx]
    neg rax
    shl rax, 2
    mov rbx, [output + rcx]
    cmp rax, rbx
    jne  not_equal

    inc rcx
    jmp check
```
- In case of non equal bytes it jumps to `not_equal` section and displays `No`
```asm
not_equal:
    mov rax, 1
    mov rdi, 1
    mov rsi, no_msg
    mov rdx, no_len
    syscall

    jmp  exit
```
- If theresn't a problem it the section ends when the current byte in `input[RCX]` equals `10` which is `\n` then it jumps to `end` section and displays `Yes`
```asm
end:
    mov rax, 1
    mov rdi, 1
    mov rsi, yes_msg
    mov rdx, yes_len
    syscall
```

# Solution
- All what we have to do is to reverse the shifting operation then reversing the `neg` instruction for each byte


# Solve script
```py
data = [
    0xfffffffffffffe34, 0xfffffffffffffe60, 0xfffffffffffffe6c, 0xfffffffffffffe50,
    0xfffffffffffffe50, 0xfffffffffffffe4c, 0xfffffffffffffe7c, 0xfffffffffffffe30,
    0xfffffffffffffe6c, 0xfffffffffffffe34, 0xfffffffffffffe14, 0xfffffffffffffe24,
    0xfffffffffffffe60, 0xffffffffffffff40, 0xfffffffffffffe84, 0xfffffffffffffe34,
    0xffffffffffffff30, 0xffffffffffffff3c, 0xfffffffffffffef0, 0xfffffffffffffe84,
    0xffffffffffffff30, 0xffffffffffffff2c, 0xffffffffffffff2c, 0xfffffffffffffe4c,
    0xfffffffffffffe78, 0xfffffffffffffed0, 0xfffffffffffffe1c, 0xfffffffffffffe84,
    0xffffffffffffff3c, 0xffffffffffffff2c, 0xfffffffffffffe84, 0xfffffffffffffe60,
    0xffffffffffffff30, 0xfffffffffffffeb8, 0xfffffffffffffef0, 0xffffffffffffff04,
    0xfffffffffffffe0c
]

for x in data:
    original_value = 0x100 - (0xFF & (x >> 2))
    print(chr(original_value), end="")
```

# Flag
> shellmates{wh0_s41D_455mbLy_15_h4RD?}