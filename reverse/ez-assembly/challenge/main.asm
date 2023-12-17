section .data
    output dq 0xfffffffffffffe34, 0xfffffffffffffe60, 0xfffffffffffffe6c, 0xfffffffffffffe50, 0xfffffffffffffe50, 0xfffffffffffffe4c, 0xfffffffffffffe7c, 0xfffffffffffffe30, 0xfffffffffffffe6c, 0xfffffffffffffe34, 0xfffffffffffffe14, 0xfffffffffffffe24, 0xfffffffffffffe60, 0xffffffffffffff40, 0xfffffffffffffe84, 0xfffffffffffffe34, 0xffffffffffffff30, 0xffffffffffffff3c, 0xfffffffffffffef0, 0xfffffffffffffe84, 0xffffffffffffff30, 0xffffffffffffff2c, 0xffffffffffffff2c, 0xfffffffffffffe4c, 0xfffffffffffffe78, 0xfffffffffffffed0, 0xfffffffffffffe1c, 0xfffffffffffffe84, 0xffffffffffffff3c, 0xffffffffffffff2c, 0xfffffffffffffe84, 0xfffffffffffffe60, 0xffffffffffffff30, 0xfffffffffffffeb8, 0xfffffffffffffef0, 0xffffffffffffff04, 0xfffffffffffffe0c
    input resb 38

section .text
    global _start

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

not_equal:
    mov rax, 1
    mov rdi, 1
    mov rsi, no_msg
    mov rdx, no_len
    syscall

    jmp  exit

end:
    mov rax, 1
    mov rdi, 1
    mov rsi, yes_msg
    mov rdx, yes_len
    syscall

exit:
    mov rax, 60
    xor rdi, rdi
    syscall

section .data
    prompt db 'Enter flag: ', 0
    prompt_len equ $ - prompt

    yes_msg db 'Yes', 0
    yes_len equ $ - yes_msg

    no_msg db 'No', 0
    no_len equ $ - no_msg
