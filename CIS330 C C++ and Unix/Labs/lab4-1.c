#include <stdio.h>
#include <stdlib.h>

void increment1(int x, int y) { x++; y++; }
void increment2(int &x, int &y) { x++; y++;}
void increment3(int *x, int *y); { (*x)++; (*y)++; }


int main(int argc, char **argv) {	
	int* x, y;
	x = 6;
    y = 4;
     
	increment1(int x, int y);
    increment2(int &x, int &y);
    increment3(int *x, int *y);

	// Deallocate memory
	for (i = 0; i <= size; i++)
		free(num[i]);
	free(num);
} // main




















