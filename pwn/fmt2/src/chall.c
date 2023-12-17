#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
}

void win(void) {
    execve("/bin/sh", NULL, NULL);
}

int main(){
    char buf[0x48] = { '\0' };

    setup();
    
    puts("Echo as a Service 2.0!");

    for (int i = 0; i < 10; i++) {
        printf("> ");
        fgets(buf, 0x48, stdin);
        printf(buf);
        if (0 == strncmp(buf, "exit\n", 0x48)) {
            break;
        }
    }

    return 0;
}
