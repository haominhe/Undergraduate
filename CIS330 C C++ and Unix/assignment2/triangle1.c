/* Winter2016 CIS330 Assignment2 Haomin He */
/* Problem 1*/
/* triangle1.c: implement the print5Triangle function */

/* In the function, declare a static 2-D array of integers and initialize its 
contents to be as shown in the example output below (for Problem 1), then print
them to standard output.
*/

#include <stdio.h>
#include "triangle.h"

void print5Triangle(){
     char triangleArr[5][9] = { 
          {' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' '}, 
          {' ', ' ', ' ', '0', '1', '2', ' ', ' ', ' '}, 
          {' ', ' ', '0', '1', '2', '3', '4', ' ', ' '}, 
          {' ', '0', '1', '2', '3', '4', '5', '6', ' '}, 
          {'0', '1', '2', '3', '4', '5', '6', '7', '8'}       
          }; // triangleArr 
     
     printf("Problem 1 (a triangle of height 5): \n");
     int i, j;
     for (i = 0; i < 5; i++){
         for(j = 0; j < 9; j++){
               printf("%c ", triangleArr[i][j]);
               } // inner for
         printf("\n");
         } // outer for
            
     } // print5Triangle
     
     

     
     
     
     
     
     
     
     
     
