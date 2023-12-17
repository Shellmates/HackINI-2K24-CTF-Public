#include <stdio.h>
#include <stdlib.h>
#include "time.h"


// A lot of functionalities must be added, I really don't wanna do this school project T-T

struct person
{
    char name[64] ;
    void (*sport)();
};

struct person *person = NULL ;

void run(){
    puts("Let's run 10km today !") ;
}

void volley(){
    puts("Volley ball is my favorite sport !") ;
}

void swim(){
    puts("I wanna swim !") ;
}

void sleeep(){
    puts("I wanna sleep :))") ;
}

void choose_sport() {
    puts("Choose your favorite sport !");

    puts("0- Running.");
    puts("1- Volley Ball.");
    puts("2- Swimming.");
    puts("3- Sleeping.");

    printf("Choice: ") ;

    int c ;
    scanf("%d",&c) ;

    switch(c){
        case 0:
            person->sport=&run ;
            break ;
        case 1:
            person->sport=&volley ;
            break;
        case 2:
            person->sport=&swim ;
            break ;
        case 3:
            person->sport=&sleeep ;            
            break;
        
        default:
            puts("Wrong number") ;
            break ;
    }

}

void do_sport(){
    if (person->sport==NULL){
        puts("You need to choose a sport first") ;
    } else {
        (*(person->sport))() ;
    }

}

void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
    srand(time(NULL)) ;

    person = (struct person*) malloc(sizeof(struct person)) ;
    person->sport = NULL ;


    if (person==NULL){
        puts("Error while allocating memory") ;
        exit(-1) ;
    }

}

void win(){
    system("/bin/sh");
}

int menu(){
    int choice ;
    puts("1- Set Name.");
    puts("2- Choose sport.");
    puts("3- Do sport.");
    puts("4- quit.");
    printf("Choice: ") ;
    scanf("%d",&choice) ;

    return choice ;
}

void setName(){

    printf("Your name: ");
    scanf("%s",person->name) ;
    puts("Name set correctly !") ;

}


int main(){
    setup() ;
    int c ;
    while(1){
        c = menu() ;
        switch (c){
            case 1:
                setName() ;
                break;
            case 2:
                choose_sport() ;
                break;
            case 3:
                do_sport() ;
                break;
            default:
                puts("see ya :))") ;
                exit(0) ;
                break;
        }
    }
    
    return 0 ;
}