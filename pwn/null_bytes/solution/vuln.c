#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <errno.h>

char impossible = 1;
typedef enum { Close , Add , Check, Exit } Path;
Path choice;

void good_job() {
    system("/bin/sh");
}

void init() {
    alarm(120);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void check(){

    char fake_flag[128]={0};
    char flag[128]={0};

    init();

    printf("Come on you should know the flag now :( :\n");

    FILE *flag_file = fopen("./flag.txt", "r");
    if (flag_file == NULL) exit(-1);
    size_t length = fread(flag, 1, 120, flag_file);

    scanf("%128s", fake_flag);

    if (strncmp(fake_flag, flag, length) == 0) {
        printf("GG's you got a shell :) :\n");
        good_job();
    } else {
        puts("N0 shell for you :/ \n");
    }
}
void impossible_check(){
    if (impossible == 0){
        printf("wow you did it \n");
        check();
    }
    else{
        printf("Not yet :(");
    }
}
int main(void) {
    init();
    choice = Close;

    while (true){
        printf("Impossible number : %d\n",impossible);
        printf("Choose :\n1- +1 \n2- Check your number \n3- Exit\n");
        scanf("%d", &choice);
        switch (choice) {
            case Add:
                impossible++;
                break;
            case Check:
                impossible_check();
                break;
            case Exit:
                exit(0);
            default:
                printf("Invalid choice\n");
                return 1;
        }
    } 
}

