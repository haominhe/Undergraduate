/* Winter2016 CIS330 Assignment2 Haomin He */
/* Problem 2*/
/* triangle1.c: implement the print5Triangle function */

/* In the function, define 2-D array by using pointers and dynamic memory 
allocation. 
*/

#include <stdio.h> // for printf
#include <stdlib.h> // for malloc
#include "triangle.h"


/* Allocate a triangle of height "height" (a 2-D array of int) */
void allocateNumberTriangle(const int height, int ***triangle){
     int i;
     (*triangle) = (int **) malloc (height * sizeof(int *));
     for(i = 0; i < height; i++){
           // number of columns = 9
           (*triangle)[i] = (int *) malloc (9 * sizeof(int)); 
           } // for   
     } // allocateNumberTriangle
     
     

/* Initialize the 2-D triangle array */
void initializeNumberTriangle(const int height, int **triangle){
     
     int triangleArr[5][9] = { 
          {' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' '}, 
          {' ', ' ', ' ', '0', '1', '2', ' ', ' ', ' '}, 
          {' ', ' ', '0', '1', '2', '3', '4', ' ', ' '}, 
          {' ', '0', '1', '2', '3', '4', '5', '6', ' '}, 
          {'0', '1', '2', '3', '4', '5', '6', '7', '8'}        
          }; // triangleArr 
          
     int i, j;     
     for(i = 0; i < height; i++){
           // number of columns = 9
           for(j = 0; j < 9; j++){
                 triangle[i][j] = triangleArr[i][j];
               } // inner for
           } // outer for 
           
     } // initializeNumberTriangle




/* Print a formatted triangle */
void printNumberTriangle(const int height, int **triangle){
     int i, j;     
     for(i = 0; i < height; i++){
           // number of columns = 9
           for(j = 0; j < 9; j++){
                 printf("%c ", triangle[i][j]);
               } // inner for
           printf("\n");
           } // outer for 
     
     } // printNumberTriangle




/* Free the memory for the 2-D triangle array */
void deallocateNumberTriangle(const int height, int **triangle){
     //All done, free it
     int i;
     for(i = 0; i < height; ++i){
          free(triangle[i]);
          } //for 
     free(triangle);
     
     } // deallocateNumberTriangle 






     
     

     
     
     
     
     
     
     
     
     
