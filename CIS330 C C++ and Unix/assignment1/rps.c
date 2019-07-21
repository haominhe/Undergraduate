/* File: rps.c */
/* Winter2016 CIS330 Assignment1 Haomin He */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>      
#include <string.h>
    
char* getUserChoice() {
    /* Prompt the user "Enter rock, paper, or scissors: " and return
       the string they enter */
    /* Maximum size of string for storing user input */
    const int maxBufSize = 30;
    char *userInput = (char *) malloc (maxBufSize * sizeof(char));
    printf("Enter rock, paper, or scissors: ");
    fgets(userInput, maxBufSize, stdin);
    
    // function char *strtok(char *str, const char *delim) breaks string str 
    // into a series of tokens using the delimiter delim.
    strtok(userInput, "\n");
    // Documentation: Stackoverflow "Removing trailing newline character from fgets() input"
    
    // Converts all letters from given string into equivalent lowercase letters
    int i;
    for(i = 0; userInput[i]; i++){
        userInput[i] = tolower(userInput[i]);
        }
    // Documentation: Stackoverflow "c - convert a mixed-case string to all lower case" 
    
    
    if (strcmp(userInput, "rock") == 0) { 
       // do nothing
    } else if (strcmp(userInput, "paper") == 0){
       // do nothing
    } else if (strcmp(userInput, "scissors") == 0){
       // do nothing
    } else {
       printf("Invalid user choice, you must enter rock, paper, or scissors.\n");
       exit(0); 
       // function void exit(int status) terminates the calling process immediately
    }        
    
    return userInput;
}

char* getComputerChoice() {
    /* void srand(unsigned int seed) seeds the random number generator
       used by the function rand */ 
    srand (time(NULL));
    /* get a pseudo-random integer between 0 and 2 (inclusive) */
    int randChoice = rand() % 3;

    /* If randChoice is 0, return "rock"; if randChoice is 1, 
     return "paper", and if randChoice is 2, return "scissors". */
    if (randChoice == 0) {
       return "rock";
    } else if (randChoice == 1) {
       return "paper";
    } else if (randChoice == 2) {
       return "scissors";
    } else {
       return "Errors happen";
    }

}

char* compare(char* choice1, char* choice2) 
{
    /* Implement the logic of the game here. If choice1 and choice2
     are equal, the result should be "This game is a tie."

     Make sure to use strcmp for string comparison.
     */
     if (strcmp(choice1, choice2) == 0) { // the contents of both strings are equal 
        return "This game is a tie.";        
     } else {
            
            if (strcmp(choice1, "scissors") == 0 && strcmp(choice2, "paper") == 0 ||
                strcmp(choice2, "scissors") == 0 && strcmp(choice1, "paper") == 0) {
                return "Scissors win.";
            } else if (strcmp(choice1, "paper") == 0 && strcmp(choice2, "rock") == 0 ||
                       strcmp(choice2, "paper") == 0 && strcmp(choice1, "rock") == 0) {
                       return "Paper wins.";                       
            } else if (strcmp(choice1, "rock") == 0 && strcmp(choice2, "scissors") == 0 ||
                       strcmp(choice2, "rock") == 0 && strcmp(choice1, "scissors") == 0) {
                       return "Rock wins.";
            } else {
                   return "Errors happen";
            }            
     }
                         
}

int main(int argc, char** argv) 
{
    char *userChoice = NULL, *computerChoice = NULL, *outcome = NULL;

    userChoice = getUserChoice();
    computerChoice = getComputerChoice();

    outcome = compare(userChoice, computerChoice);

    printf("You picked %s.\n", userChoice);
    printf("Computer picked %s.\n", computerChoice);
    printf("%s\n", outcome);

    free(userChoice);
    system("pause");
    return 0;
} 
