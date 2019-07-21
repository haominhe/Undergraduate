/*
 * CIS 314 Fall 2015 Lab 1
 * Assigned project
 * 
 * Haomin He
 *
 * This program reads a sorted array from a file and finds a requested number
 *    using recursive or iterative binary search. The array is read from a file
 *    defined by FILE_NAME, which should be written as the number of elements
 *    followed by the elements themselves. each number can be deliniated with
 *    any whitepace character. Also, the maximum size of the array is defined 
 *    as MAX_SIZE.
 * 
 * NOTE: The array must be sorted!!
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 150
#define FILE_NAME "array.dat" //must include quotes

// Implement the rest of the program
int iterativeBinSearch(int Iterarray[], int IterrequestNum, int lowerbound, int upperbound);
int recursiveBinSearch(int Recarray[], int RecrequestNum, int lowerBound, int upperBound);

int main(void) {

   FILE *in_file; //
   int array[MAX_SIZE];
   int size;
   char in_file_name[] = FILE_NAME;

   printf("\n\n=== CIS314 Fall 2014 - Lab 1: Part 2: Program 2 ===\n\n");


   printf("\nStudent: Haomin He\n\n");
   
   //1. Reads an array of integers from a file
   ////////////////////// read the file "array.dat"
   int gotInt = 0;
   int i = 0;
   int lengthArray = 0; 

   in_file = fopen (in_file_name , "r"); // read
   if (in_file == NULL) perror ("Error opening file"); // print error

   else
   {
      fscanf(in_file, "%d", &lengthArray);
      printf("Length of this array %d \n", lengthArray);

     if (in_file)
     {
       while ( fscanf (in_file, "%d" , &gotInt) != EOF ){ // end of file
       
       array[i] = gotInt; 
       i++;}
     }
     lengthArray = i; 
     fclose (in_file);
   }
   

   //Displays the array
   printf("The array read from file array.dat: \n");
   int k;
   for (k = 0; k < lengthArray; k ++){
       printf("%d ", array[k]);}
    
    //////////////////// finds a requested number
    int requestNum;
    printf("\n\nEnter the number you want to find in the file: \n");
    scanf("%d", &requestNum);
        
   //////2. Performs a binary search on an array iteratively and recursively
   // iterative binary search
   int delta1;
   clock_t t1, t2;
   t1 = clock();
   int iterativeSpeed;
   iterativeSpeed = iterativeBinSearch(array, requestNum, 0, lengthArray);
   t2 = clock();
   delta1 = t2 - t1;
   
   // recursive binary search
   int delta2;
   clock_t t3, t4;
   t3 = clock();
   int recursiveSpeed;
   recursiveSpeed = recursiveBinSearch(array, requestNum, 0, lengthArray);
   t4 = clock();
   delta2 = t4-t3;
   
   // 3. Displays the results, and execution times.
   
   printf("\nIterative binary search result: %d, Execution time: %d", iterativeSpeed, delta1);
   printf("\nRecursive binary search result: %d, Execution time: %d\n", recursiveSpeed, delta2);
   
   return 0;
}


int iterativeBinSearch(int Iterarray[], int IterrequestNum, int lowerbound, int upperbound){
    int middle;
    while(lowerbound <= upperbound){
          middle = (lowerbound + upperbound)/ 2;
          if (middle == IterrequestNum){
              return middle;}// if
          else if (Iterarray[middle] < IterrequestNum){
               lowerbound = middle + 1;}//else if
          else {
               upperbound = middle - 1;}//else
          
          }// while
    return -1; // not found the requested number
    } // end of function




int recursiveBinSearch(int Recarray[], int RecrequestNum, int lowerBound, int upperBound){
    int middle;
    
    // base case
    if(lowerBound > upperBound){
       return -1; }// not found the requested number // if
       
    middle = (lowerBound + upperBound)/2;
    if(Recarray[middle] == RecrequestNum){
        return middle;}// if
    else if(Recarray[middle] < RecrequestNum){
         return recursiveBinSearch(Recarray, RecrequestNum, middle + 1, upperBound);}// else if
    else {
         return recursiveBinSearch(Recarray, RecrequestNum, lowerBound, middle - 1);}//else
    } // end of function















