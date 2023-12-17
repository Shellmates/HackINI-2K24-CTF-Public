#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define PASSWORD_LENGTH 4096

// Function to generate a random 12-bit password
int generateRandomPassword()
{
    return rand() & 0xFFF; // Generate a 12-bit random number
}

// Function to check for a specific 12-bit sequence
int checkSequence(char *password, int length, int targetSequence)
{
    // Convert the sequence to an integer
    
    for (int i = 0; i < length+1; i++)
    {
        char extracted[13];
        strncpy(extracted,&password[i] , 12);
        extracted[12] = '\0';
        
        long int passwordInt = strtol(extracted, NULL, 2);
        

        if (targetSequence == passwordInt)
        {
            return 1; // Target sequence found
        }
    }
    return 0; // Target sequence not found
}
void disable_buffering(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
int main()
{
    disable_buffering();
    srand((unsigned int)time(NULL)); // Seed initialization with current time

    for (int stage = 1; stage <= 12; stage++)
    {
        int generatedPassword = generateRandomPassword();

        char userPassword[PASSWORD_LENGTH + 1]; // Password length + '\0'
        printf("===========Stage %d===========\n", stage);
        printf("Enter the Password: ");
        fgets(userPassword, sizeof(userPassword), stdin);
        userPassword[strcspn(userPassword, "\n")] = '\0'; // Remove trailing newline character
        int length = strlen(userPassword);
        int result = checkSequence(userPassword, length, generatedPassword);

        if (result)
        {
            printf("Stage %d - Password Matched!\n\n", stage);
        }
        else
        {
            printf("Password Not Matched! Try Again!! \n\n", stage);
            exit(1);
        }
    }

    puts("Congratulations! You have completed all the stages!");
    FILE *flagFile = fopen("flag.txt", "r");
    if (flagFile != NULL)
    {
        char flagContent[50]; // Assuming maximum content size of 100 characters
        fgets(flagContent, sizeof(flagContent), flagFile);
        fclose(flagFile);
        printf("Here is your Prize: %s\n", flagContent);
    }
    else
    {
        printf("Flag file not found.\n");
    }
    return 0;
}
