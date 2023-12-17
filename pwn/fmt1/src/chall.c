#include <stdio.h>
#include <stdlib.h>

void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
}

int main(){
    FILE* file = NULL;
    char flag[0x100] = { '\0' };
    char buf[0x40] = { '\0' };

    setup();
    
    file = fopen("flag.txt","r");
    if (file == NULL){
        puts("Cannot open flag.txt");
        exit(1);
    }
    fgets(flag, 0x100, file);

    puts("Echo as a Service!");

    for (int i=0; i < 10; i++) {
        printf("> ");
        fgets(buf, 0x40, stdin);
        printf(buf);
    }

    return 0;
}
