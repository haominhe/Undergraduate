#include <stdio.h>


double power(double a, double b) {
       int i, result = 1;
       for (i = 0; i < b; i++){ 
           result *= a;
           }
       return result; 
       }


/*int main(int argc, const char * argv[])
{
    printf("%s\n", outcome ? "true" : "false");
    system("pause");

    return 0;
}*/
 
