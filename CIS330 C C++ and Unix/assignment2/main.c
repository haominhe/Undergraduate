#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "triangle.h"
#include "triangle2.h"

#include "triangle1.c"
#include "triangle2.c"

void clearInputBuffer() {
  while ( getchar() != '\n' );
}

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
}

int main() {
  int i=0, height = 0, numInts=0;
  int **triangle;

  // Problem 1
  printf("Problem 1 (a triangle of height 5):\n"); /* Fixed-size square */
  print5Triangle();

  // Problem 2
  printf("\nProblem 2:\n"); /* Flexible-height triangle */
  height = getInt("Please enter the height of the triangle [1-5]: ", 1, 5);

  allocateNumberTriangle( (const int) height, &triangle );
  initializeNumberTriangle( (const int) height, triangle );
  printNumberTriangle( (const int) height, triangle );

  // Free memory allocated earlier
  deallocateNumberTriangle( (const int) height, triangle );
  
  system("pause");
  return 0;
} 
