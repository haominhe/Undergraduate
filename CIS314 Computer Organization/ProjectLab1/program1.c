/*
 * CIS 314 Fall 2015 Lab 1
 * Assigned project
 *
 * Haomin He 
 *
 * (Almost) Universal Base Convertor
 * This program converts a x base to y base converter [less than 16]. 
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define MAX_NUM 16
#define MAX_DECIMAL 2147483647 //for int

// Implement the rest of the program

//function headers
int convert_to_decimal(char inputnum[], int inputbase);
int convert_to_userbase(int aDecimalNum, int outputbase);


int main(){

	char in_number[MAX_NUM+1];
	int in_base = 0;
	int out_base = 0;
	// char out_number[MAX_NUM+1]; use this variable in the fuction convert_to_userbase
	
	printf("(Almost) Universal Base Convertor\n");
//////////////////////////////////////////////////   
    printf("Please enter the number base (binary to hexadecimal): \n");
    scanf("%d", &in_base);
    if (in_base < 2 || in_base > 16) {
                printf("I/O base is out of range (2-16), please restart the program \n");
       }
    if (isalpha(in_base)){
           printf("You have entered an invalid base, please restart the program \n");
           }
    
 ///////////////////////////////////////////////  
    printf("Please enter the number you want to convert: \n");
    scanf("%s", in_number);
    if (*in_number > (MAX_DECIMAL)) {
                  printf("Input number is too large to be converted/overflow, please restart the program \n");
       }
    
 /////////////////////////////////////////////  
    printf("Please enter a base you want to convert to (binary to hexadecimal): \n");
    scanf("%d", &out_base);
    if (out_base < 2 || out_base > 16) {
                printf("I/O base is out of range (2-16), please restart the program\n");
       }
    if (isalpha(out_base)){
           printf("You have entered an invalid base, please restart the program\n");
    }
////////////////////////////////////////////		
	// Takes a number and its base from the user and convert the number into 
    // decimal. It should be able to use any base system from binary to hexadecimal.
    int gotDecimalNum = 0;
    gotDecimalNum = convert_to_decimal(in_number, in_base);
	 
    printf("This is the dicimal number from your input number %d\n", gotDecimalNum);
    
    // Convert the decimal number from task 1. into any user-defined base (
    // binary to hexadecimal).
    convert_to_userbase(gotDecimalNum, out_base);
    
    
    printf("\n");

     return 0;
}


int convert_to_decimal(char inputnum[], int inputbase){ 
    // if the user type in hexadecimal, it may contain letter
    if (inputbase == 16){
        int hexFinalVal = 0;
        //////////////////////////
        int lengthArray = 0;
        char *aValueStr;
        for (aValueStr = inputnum; *aValueStr != '\0'; ++aValueStr){
            ++lengthArray;} // got the length of the input hexadecimal
        
        aValueStr = inputnum;
        int i;    // if the current letter is not none and i is less than the 
                  // length, find the corresponding hexadecimal
        for(i = 0; *aValueStr != '\0' && i < lengthArray; ++i, ++aValueStr){
              if (*aValueStr >= 48 && *aValueStr <= 57){ //0-9
                   hexFinalVal += (((int)(*aValueStr)) - 48) * pow(16, lengthArray - i - 1);}
                   
              else if (*aValueStr >= 65 && *aValueStr <= 70) { //A-F
                   hexFinalVal += (((int)(*aValueStr)) - 55) * pow(16, lengthArray - i - 1);}
              else if (*aValueStr >= 97 && *aValueStr <= 102){ //a-f
                   hexFinalVal += (((int)(*aValueStr)) - 87) * pow(16, lengthArray - i - 1);}
              else {printf("Please restart the program, the input number is unacceptable \n");}
              }
        return hexFinalVal;
        
        
    } else {
        // convert String to Integer using the atoi function
        int digitInputNum = atoi(inputnum);
        int decimaloutput = 0, i = 0, remainder;
        
        while(digitInputNum != 0){
             remainder = digitInputNum % 10;
             digitInputNum = digitInputNum / 10;
             decimaloutput += remainder * pow(inputbase, i);
             ++i;
                }
        return decimaloutput;
       }
}

// Use a global char array to represent possible digits
static char allDigit[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};

// Combine tasks 1. And 2. into a program/function that converts an input number
// from any user-defined base to another (binary to hexadecimal).
int convert_to_userbase(int aDecimalNum, int outputbase) {
    char out_number[MAX_NUM+1];
    int remain;
    int i = 1;
       
    while(aDecimalNum != 0) {
         
         remain = aDecimalNum % outputbase; // the remainder
         out_number[i++] = allDigit[remain]; // get the corresponding number from the global variable
         aDecimalNum = aDecimalNum / outputbase; // the quotient
         }
    printf("This is the user-defined base output number ");
    int j = 0;
    for (j = i - 1; j > 0; j--){
        printf("%c", out_number[j]);}
          
    return 0;   
}






















