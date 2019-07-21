/* CIS 330 Lab 7 Haomin He
*/ 

#include <iostream>
#include <string>
#include <cstdlib> // rand - Returns a pseudo-random integral number 
#include <vector>
#include <algorithm>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
using namespace std;

/*
Write a print function that accepts const std::vector<int> & and prints the 
elements of the vector, using the iterator std::vector<int>::const_iterator. 
For this function, you should not use the index operator [] directly (when using 
a for loop, the performance of the iterator is typically better than the 
[] operator).
*/

void printVector(const vector<int> & Avector){
     cout << "This vector contains: "<< endl;
     for(vector<int>::const_iterator it = Avector.begin(); it != Avector.end(); ++it){
        cout << ' ' << *it;}
     cout << '\n';
     
        
     } // printVector





int main() {
    // initialize random seed
    srand((unsigned)time(NULL));
    // add 15 random integers into that container
    vector<int> v (15); 
    
    
    cout << "Initializing the vector" << endl;
    vector<int>::iterator it;
    for(it = v.begin(); it != v.end(); ++it) {
           // it is a pointer to the current object
           *it = rand();
           cout << ' ' << (*it); 
           
           } // for
           cout << endl;
    
    cout << "Print the random values of the vector v, using function printVector" << endl;
    printVector(v);
    
    cout << "\nPrint the sorted result." << endl;
    sort(v.begin(), v.end());
    printVector(v);
    
    cout << "\nDefine a new std::vector<int> variable vCopy. Use the std::copy" << endl;
    cout << "function to make copy of v into vCopy. Print the values in vCopy" << endl;
    vector<int> vCopy (15);
    // vCopy = v or
    copy(v.begin(), v.end(),vCopy.begin());
    printVector(vCopy);
    
    cout << "\nUse the std::random_shuffle function to shuffle the values in "<< endl;
    cout << "vCopy. Note that the previous values in v was sorted. Print the values in vCopy."<< endl;
    random_shuffle(vCopy.begin(), vCopy.end());
    printVector(vCopy);
    
    cout << "\nHere is the original v" << endl;
    printVector(v);
    
    return 0;
    } // main









