#include <stdio.h>
#include <stdlib.h>


// compiled with: gcc chall.c -o chall -fno-stack-protector -no-pie -m32

void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
}


void get_flag(){
    FILE* fd = fopen("flag.txt","r");

    if (fd==NULL){
        printf("Error while openning flag.txt\n") ;
        exit(-1) ;
    }

    char flag[0x100];

    fgets(flag,0x100,fd) ;

    printf("%s\n",flag);

    exit(0) ;
}

void vuln(){

    char buf[64] ;
    int a =0 ;


    gets(buf) ;

    if (a==0xdeadbeef){
        get_flag() ;
    
    } else if ( a != 0){

        puts("so cloooooose") ;

    } else {

        puts("nope buddy") ;

    }

    exit(0) ;

}

int main(){
    setup() ;
    puts("Welcome to pwn World !");
    printf("Enter your name: ") ;

    vuln() ;

    return 0 ;

}