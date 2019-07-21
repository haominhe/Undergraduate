/* Winter2016 CIS330 Assignment5 CIS330 Game of Livestock
   Haomin He */
/* Problem 1*/
/* main.cpp: a main file of the Game of Life */

/*
-Run the game by performing a certain number of steps, which are specified as a 
parameter.
-Use arrays or STL containers to represent the grid, for example a vector of 
vectors of char, where 'S' designates a sheep, 'W' designates a wolf, and 'F' 
designates a farmer (and '.' designates an empty cell).
-Create a Makefile to compile your source files into .o files.
*/


#include "game.hpp"
#include <iostream> 
#include <vector>
using namespace std; // Example: can write just cout instead of std::cout when 
// calling the operator cout defined in the namespace std .


int main() {
    // read size input of the grid from the user
    // row and column
    int rowInput = 0;
    int columnInput = 0;
    // cout	standard output stream
    cout << "Please enter the size of the grid (int int): " << endl;
    cin >> rowInput >> columnInput;
    
    // read number of steps 
    int stepInput = 0;
    cout << "Please enter the number of steps (int): " << endl;
    cin >> stepInput; 
    
    Game game(rowInput, columnInput);
    game.randomGrid();
    game.display();
    int counter;
    for(counter = 1; counter <= stepInput; ++counter) {
       game.checkRules();
       cout << "\n" << endl;
       cout << "Step " << counter << ":" << endl;
       game.display(); 
       } // for
   
    
    
    
    return 0;    
    } // main





























