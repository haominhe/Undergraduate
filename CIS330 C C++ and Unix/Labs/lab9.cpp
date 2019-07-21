/* CIS 330 Lab 9 Haomin He
*/ 

#include <iostream>
#include <string>
#include <cstdlib> // rand - Returns a pseudo-random integral number 
#include <vector>
#include <algorithm>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <unistd.h> // fork()
using namespace std;
#include <sys/types.h>


/*
Write a main function with an int array of size 10. Fill the array with random 
values. Print the sum of the values.
Then use fork to create a child process.  
     
In child process add the elements 0-4 from array and save the result in a fie out.txt
In the parent process add the elements 5-9 from array. Wait for the child 
process to finish writing and closing the out.txt file. Then open the file 
in parent process and get the total value of elements 0-4. Using this number 
print the sum of the values of the whole array (elements 0-9).
*/



int main() {
    int intArray[10];
    int counter;
    srand(time(NULL));
    int sumval = 0;
    
    for (counter = 0; counter < 10; ++counter) {
        intArray[counter] = rand() % 100 + 1;
        sumval += intArray[counter];
        cout << intArray[counter] << endl;
        } // for
    cout << sumval << endl;
        
    int ctr = 0;
    pid_t pid = fork();
    
    if (pid == 0) {
      // for (counter = 0; counter < 5; ++counter) {
        // intArray[counter]
        cout << "From child" << endl;
       // } // for
       
       } // if child
    else {
          cout << "From parent" << endl;
          } // else parent
    
    
    system("pause"); 
    return 0;
    } // main















