#include <stdio.h>
#include <stdlib.h>


// compiled with: gcc chall.c -o chall -fno-stack-protector -no-pie -m32

void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
}

void vuln(){

    char buf[64] ;

    gets(buf) ;

}

int main(){
    setup() ;
    puts("Welcome to pwn World !");
    printf("Gift for ya: %p\n",puts);
    printf("Enter your name: ") ;

    vuln() ;


    return 0 ;

}