#include <stdio.h>
#include <stdbool.h>

#define ROW 3
#define COL 4

bool arrayEqual(int a[ROW][COL], int b[ROW][COL], int m, int n)
{    
     // function bool arrayEqual that compares two 2D arrays
     // (m and n are the size of the rows and columns correspondingly)
     // It returns true if all the corresponding elements are equal in a and b, 
     // otherwise false.
     const int numRows = m, numColumns = n;
     int i, j;
     
     for (i = 0; i < numRows; i++) {
         for (j = 0; j < numColumns; j++) {
             if (a[i][j] != b[i][j]){
                return false;
             } // if
         }// for
     }// for 
     return true;     
     
}

int main(int argc, const char * argv[])
{

    int a[ROW][COL] = {
        {0, 1, 2, 3} ,
        {4, 5, 6, 7} ,
        {8, 9, 10, 11}
    };

    int b[ROW][COL] = {
        {0, 1, 2, 3} ,
        {4, -1, 6, 7} ,
        {8, 9, 10, 11}   
    };
    
    // put your code here ...
    bool outcome;
    outcome = arrayEqual(a, b, ROW, COL);
    printf("%s\n", outcome ? "true" : "false");
    system("pause");

    return 0;
}
