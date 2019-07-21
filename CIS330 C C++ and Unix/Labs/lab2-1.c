#include <stdio.h>
#include <stdbool.h>

#define ROW 3
#define COL 4

bool arrayEqual(int **a, int **b, int m, int n, int *y)
{
     // function bool arrayEqual that compares two 2D arrays
     // (m and n are the size of the rows and columns correspondingly)
     // It returns true if all the corresponding elements are equal in a and b, 
     // otherwise false.
     // put your code here ...
     
     const int numRows = m, numColumns = n;
     int i, j;
     
     for (i = 0; i < numRows; i++) {
         for (j = 0; j < numColumns; j++) {
             if (a[i][j] != b[i][j]){
                *y = a[i][j];
                return false;
             } // if
         }// for
     }// for 
     return true;
}

//  Initialize two arrays (e.g. 3*4 dimension)
int main(int argc, const char * argv[])
{
    
     int **numbers; 
     const int numRows = ROW, numColumns = COL;
     int i,j;
     
     numbers = (int **) malloc ( numRows * sizeof(int *) );
     for (i = 0; i < numRows; i++) {
         numbers[i] = (int *) malloc ( numColumns * sizeof(int) );
         for (j = 0; j < numColumns; j++) {
             numbers[i][j] = 6;
             }
     }// for 
     
     
     
     
     
     int **numbers0; 
     const int numRows0 = ROW, numColumns0 = COL;
     int ii,jj;
     
     numbers0 = (int **) malloc ( numRows0 * sizeof(int *) );
     for (ii = 0; ii < numRows0; ii++) {
         numbers0[ii] = (int *) malloc ( numColumns0 * sizeof(int) );
         for (jj = 0; jj < numColumns; jj++) {
             numbers0[ii][jj] = 6;
             }
     }// for 
     

    int y = 0;
   
    bool outcome;
    outcome = arrayEqual(numbers, numbers0, ROW, COL, &y);
    printf("%s\n", outcome ? "true" : "false");
    printf("pass-by-reference argument: %d\n",y);
    system("pause");

    return 0;
}
