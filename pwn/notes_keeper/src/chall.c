#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NOTE_SIZE 0x100
#define TITLE_SIZE 0x40

typedef struct note
{
    char* title;
    char* content ;

} ;

typedef struct note note ;

note* notes[10] ;

int count = 0 ;
int MAX = 10 ;


void setup(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);

    printf("gift: %p\n",puts);
}

void viewNote(int index){
    if ((index<0)||(index>count)){
        printf("Index out of bound...");
        exit(1);
    }

    note* n = notes[index] ;
    printf("Note:\n\nTitle: %s\nContent: %s\n", n->title, n->content);

}


note* allocNote(){
    if (count < MAX){
        note* n = (note *) malloc(sizeof(note)) ;

        n->title = (char *)malloc(TITLE_SIZE) ;
        n->content = (char *)malloc(NOTE_SIZE) ;

        printf("Title: ");
        read(0,n->title,TITLE_SIZE) ;
        printf("Note: ");
        read(0,n->content,NOTE_SIZE) ;
        notes[count] = n ;

        count = count +1 ;

        return n ;

    } else {
        printf("Max notes reached ...\n");
        exit(1) ;
    }
}

void editNote(int index){

    if ((index>count)||(index<0)) {
        printf("index out of bound...\n");
        exit(1) ;    
    }

    note* n = notes[index] ;

    printf("Title: ");
    read(0,n->title,TITLE_SIZE) ;
    printf("Note: ");
    read(0,n->content,NOTE_SIZE) ;
    
}

void  deleteNote(int index){
    if ((index>count)||(index<0)) {
        printf("index out of bound...\n");
        exit(1) ; 
    }

    note* n = notes[index] ;
    free(n->title)  ;
    free(n->content);
    free(n) ;
}

int menu(){
    int choice ;
    puts("1- Create Note.");
    puts("2- Delete Note.");
    puts("3- View Note.");
    puts("4- Edit Note.");
    puts("5- Exit.");

    printf("Choice: ") ;
    scanf("%d",&choice) ;

    return choice ;
}

int main(){
    setup() ;
    int c ;
    int index ;

    while(1){
        c = menu() ;
        switch (c){
            case 1:
                allocNote() ;
                break;
            case 2:
                printf("index: ");
                scanf("%d",&index);
                deleteNote(index) ;
                break;
            case 3:
                printf("index: ");
                scanf("%d",&index);
                viewNote(index) ;
                break;
            case 4:
                printf("index: ");
                scanf("%d",&index);
                editNote(index) ;
                break ;
            case 5:
                puts("see ya");
                exit(0) ;
                break ;
            default:
                puts("see ya :))") ;
                exit(0) ;
                break;
        }
    }
    
    return 0 ;
}