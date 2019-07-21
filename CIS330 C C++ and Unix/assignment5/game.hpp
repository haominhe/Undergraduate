/* Winter2016 CIS330 Assignment5 CIS330 Game of Livestock
   Haomin He */
/* Problem 1*/
/* game.hpp: a header file of the Game of Life */

/*
Implement the Game of Livestock by defining a Game class in files game.hpp and 
game.cpp. The class should include methods for
*/

#include <vector>
#include <iostream>
using namespace std;

#ifndef GAME_HPP_
#define GAME_HPP_

// Define a Game class. Contain proper data members and functions.
class Game {
      public:
             // constructor and destructor 
             Game(int row, int column);
             ~Game();
             
             /* Create an initial set of randomly selected cell values in the 
             2-D rectangular grid: empty, sheep, wolf, farmer. */
             void display();
             void randomGrid();
             void checkRules();
             void updateCounter(int num1, int num2);
                          
      
      private:
             int row, column;
             int emptyNum, sheepNum, wolfNum, farmerNum;
             /* Use arrays or STL containers to represent the grid, for example 
              a vector of vectors of char */
             vector<vector<char> > grid;
               
      }; // Game

#endif /* GAME_HPP_ */










