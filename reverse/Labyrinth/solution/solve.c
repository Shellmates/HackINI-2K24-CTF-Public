#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


// the reverse function of "reverse" stays the same
void reverse(char* str) {
    int start = 0;
    int end = strlen(str) - 1;
    while (start < end) {
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
}

// the reverse function of reverseWords stays the same
void reverseWords(char* str) {
    char* token = strtok(str, " ");
    while (token != NULL) {
        reverse(token);
        token = strtok(NULL, " ");
    }
}

// the reverse function of "transpose" stays the same
void transpose(char* str) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; ++i) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

// the reverse function of "substitute" changes
void reverseSubstitute(char* str) {
    for (int i = 0; i < strlen(str); ++i) {
        if (isalpha(str[i])) {
            if (islower(str[i])) {
                str[i] = 'a' + (str[i] - 'a' + 5) % 26; // Reverse substitution
            } else {
                str[i] = 'A' + (str[i] - 'A' + 5) % 26; // Reverse substitution
            }
        }
    }
}

// the reverse function of "rotateRight" changes
void rotateLeft(char* str, int shift) {
    int len = strlen(str);
    shift = shift % len;
    char temp[shift + 1];
    strncpy(temp, str, shift);
    temp[shift] = '\0';
    memmove(str, &str[shift], len - shift);
    strncpy(&str[len - shift], temp, shift);
}


// used to bruteforce the order of the functions
void callFunctionsInOrder(int order[], char flag[]) {
    for (int i = 0; i < 4; i++) {
        switch (order[i]) {
            case 0:
                rotateLeft(flag, 12);
                break;
            case 1:
                transpose(flag);
                break;
            case 2:
                reverseWords(flag);
                break;
            case 3:
                reverseSubstitute(flag);
                break;
        }
    }

    printf("\n this might be the flag: %s", flag);
}

void generatePermutations(int order[], int n, char flag[]) {
    if (n == 1) {
        callFunctionsInOrder(order, flag);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (n % 2 == 1) {
            int temp = order[0];
            order[0] = order[n - 1];
            order[n - 1] = temp;
        } else {
            int temp = order[i];
            order[i] = order[n - 1];
            order[n - 1] = temp;
        }
        generatePermutations(order, n - 1, flag);
    }
}


/*





*/

int main() {

    //easily find the 6 parts using the strings command 
    //find it exactly above the output text of the main function
    // all ordered
    char part1[] = "T0p_H4Y3";
    char part2[] = "_!O}nczg";
    char part3[] = "ghvozn{O";
    char part4[] = "0jF_n0_h";
    char part5[] = "pxc_$O3k";
    char part6[] = "n_Wp";

    //concatenation of the 6 parts
    char flag[] = "T0p_H4Y3_!O}nczgghvozn{O0jF_n0_hpxc_$O3kn_Wp";


    //now we will bruteforce th eorder of the functions call using a simple use case and a for loop
    int order[] = {0, 1, 2, 3}; // Initial order of function calls
    printf("Executing all possible permutations:\n");
    generatePermutations(order, 4, flag);
    return 0;
}