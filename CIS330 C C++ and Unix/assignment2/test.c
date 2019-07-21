/* Winter2016 CIS330 Assignment2 Haomin He */
/* Problem 1 & 2*/
/* test.c: implement the main function, which should include the triangle.h 
header file and call the print5Triangle() function */

/* Compile and test your code with
gcc -std=c99 -o triangle triangle1.c test.c
./triangle


Compile and run
gcc -std=c99 -o triangle2 triangle1.c triangle2.c test.c
./triangle2
*/

#include <stdio.h>
#include "triangle.h"
#include "triangle2.h"
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>

#include "triangle1.c"
#include "triangle2.c"

// To avoid warning: implicit declaration of function
void allocateNumberTriangle(const int height, int ***triangle);
void initializeNumberTriangle(const int height, int **triangle);
void deallocateNumberTriangle(const int height, int **triangle);


int main(){
    print5Triangle(); // Test Problem 1
    printf("\n");
    printf("Problem 2: \n");
    
    // declare a variable
    int **triangle;
    int temp = 0;
    int height = 0;
    
    /* read the input, which should be a number in the range [1-5] (inclusive). 
    If they enter a different number or string, keep prompting and reading new 
    input.
    */
    
    /* Maximum size of string for storing user input */
    const int maxBufSize = 30;
    char *userInputSize = (char *) malloc (maxBufSize * sizeof(char));
    
    while(true){
                printf("Please enter the height of the triangle [1-5]: ");
                fgets(userInputSize, maxBufSize, stdin);
                // Removing trailing newline character from fgets() input
                strtok(userInputSize, "\n");
            
                if(isdigit(*userInputSize)){
                    temp = atoi(userInputSize); // convert to integer 
                    if(temp >= 1 && temp <= 5){
                                     height = temp;
                                     break;
                                     } // inner if
                    } // if
                else {
                     printf("Wrong input, please try again. \n");
                     } // else                
                } // while
    
/* For the first argument, (const int height), pass the height the user entered 
but cast it to const int first. 

Be careful with how you pass the second argument to allocateNumberTriangle -- 
it has to be a reference to triangle, i.e., &triangle.
*/

    
    /* Allocate a triangle of height "height" (a 2-D array of int) */
    allocateNumberTriangle((const int)height, &triangle);
    
    /* Initialize the 2-D triangle array */
    initializeNumberTriangle((const int)height, triangle);
    
    /* Print a formatted triangle */
    printNumberTriangle((const int)height, triangle);
    
    /* Free the memory for the 2-D triangle array */
    deallocateNumberTriangle((const int)height, triangle);
    
    
    
    free(userInputSize);
    system("pause");
    return 0;
    } 











