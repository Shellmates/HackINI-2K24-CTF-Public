#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h> 

//compiled with: gcc chall.c -o chall -fno-stack-protector -no-pie -m64
void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
}

void win(){
    char flag[59]  ; 
    FILE * file = fopen("flag.txt","r");
    fread(flag , 59,1,file);
    puts("Woah ,kifah 9dert ?");
    puts(flag) ; 
}

void check(){
    unsigned long  b,c;
    char future[15];
    puts("Checking ... ");
    ((void (*)())(uintptr_t)(*(unsigned long *)future))();  
} 
void timeTravel(){
    char agent[15];
    unsigned long month = 12;
    unsigned long year = 2023;
    printf("I heard that you can control the future.Prove it to me !\n>");
    fgets(agent, 24, stdin);
}

int main() {
    setup() ;
    timeTravel() ; 
    check();
    return 0;
}