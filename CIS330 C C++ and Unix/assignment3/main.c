/* Winter2016 CIS330 Assignment3 Haomin He */
/* Problem 3 */
/* main.c */

/* 
- Create a main.c that initializes the directory and prompts the user to add or 
  delete entries.
- Write a makefile to build your application (feel free to copy and modify the
  Makefile from assignment 2). Name the executable directory. 
*/

#include <stdio.h>
#include "directory.h"
#include <stdlib.h>
#include <string.h>
#include <limits.h>
// determines various properties of the various variable types



// codes from the assignment 2
void clearInputBuffer() {
  while ( getchar() != '\n' );
} // clearInputBuffer



// getInt()), which provides robust validation for integer input   
int getInt(const char* msg, int low, int high) {
	/* Keep prompting the user for input until they enter a single integer
	 * whose value is between low and high (inclusive).
	 */
	int numInts = 0, num = 0;
	while (numInts != 1 || num < low || num > high) {
	    printf("%s",msg);
	    numInts = scanf("%d", &num);  // returns the number of integers read from input
	    clearInputBuffer();
	}
	return num;
} // getInt



void getInput(thisPerson ** thisPerInfo1) {
     // declare possible input variables
     int inputNum = 0;
     int inputNumRemove = 0;
     
     // infinity loop - while true 
     while(1) {
             printf("Please choose an option: \n");
             printf("1. Insert a new entry. \n");
             printf("2. Delete an entry. \n"); 
             printf("3. Display current directory. \n");    
             printf("Option: \n"); 
             // get the inputs
             inputNum = getInt("> ", INT_MIN, INT_MAX);
             if (inputNum == 1) {
                 // allocate memory
                 char *nameInput = (char *) malloc(50 * sizeof(char));
			     char *numberInput = (char *) malloc(50 * sizeof(char));
                 
                 // get input
                 printf("Enter a name: ");
			     fgets(nameInput,50,stdin); 
			    
			     // get rid of the enter line
                 for(int i = 0; i < strlen(nameInput); i++){
		                 if (nameInput[i] == '\n'){
			             nameInput[i] = ' ';
	               	} // if
                 } // for
                 
    			printf("Enter a phone number: ");
		    	fgets(numberInput,50,stdin);
		    	printf("\n");
                // get rid of the enter line
                 for(int j = 0; j < strlen(numberInput); j++){
		                 if (numberInput[j] == '\n'){
			             numberInput[j] = ' ';
	               	} // if
                 } // for  
                 
                 storePeopleNameAndPhNum(*thisPerInfo1, nameInput, numberInput);
               	 free(nameInput);
	             free(numberInput);           
         
                 } // if
                 
                 
                 else if (inputNum == 2) {
                      printAllInfo(*thisPerInfo1);
                      printf("Which entry should I delete? ");
                      inputNumRemove = getInt("> ",1,INT_MAX);
                      printf("\n");
                      deleteInfo(thisPerInfo1, inputNumRemove);                       
                      } // else if
                      
                 else if (inputNum == 3) {
                      printAllInfo(*thisPerInfo1);
                      } // else if
                 
                 else {
                      printf("Sorry, you have typed an invalid data. \n");
                      printf("Please restart the program \n");
                      exit(0);
                      } // else
             } //while
     } // getInput




int main(int argc, char** argv){
    // allocate the memory
	thisPerson *phoneBook = (thisPerson*) malloc(sizeof(thisPerson));
	// initialize the values
    phoneBook->personPtr = NULL;
	phoneBook->nextPerson = NULL;
    getInput(&phoneBook);
	

	//free(phoneBook);
	return 0;
}










