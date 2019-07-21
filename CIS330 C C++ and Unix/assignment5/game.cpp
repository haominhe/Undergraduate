/* Winter2016 CIS330 Assignment5 CIS330 Game of Livestock
   Haomin He */
/* Problem 1*/
/* game.cpp: implement a variation on the Conway's Game of Life */

/*
The universe of the Game of Livestock is an infinite two-dimensional orthogonal 
grid of square cells, each of which is in one of four possible states.
A cell can be empty or dead
A cell can have a sheep in it (S)
A cell can have a wolf in it (W)
A cell can have a farmer in it (F)
*/


#include <stdio.h>
#include "game.hpp"
#include <stdlib.h>
#include <iostream> 
#include <vector>
#include <cstdlib> // random number generation - srand
#include <ctime> // help generate random number - srand((unsigned)time(NULL));

using namespace std;


// constructor - initialize all private variables
Game::Game(int rowNum, int columnNum) : row(rowNum), column(columnNum), grid(30), 
             emptyNum(0), sheepNum(0), wolfNum(0), farmerNum(0)  {  
             // nothing else to do in the constructor
             } // constructor 
             
Game::~Game() {
} // destructor





// randomly selected cell values in the grid
void Game::randomGrid(){
     /* in order to generate random-like numbers, srand is usually initialized
     to some distinctive runtime value
     unsigned - only represent positive values */
     srand((unsigned)time(NULL));
     
     // since we have 4 characters to represent, we use modulus operator 
     int remainder = 0;
     int i, j;
     for(i = 0; i < this->row; ++i) {
             grid[i] = vector<char>(30);
             for(j = 0; j < this->column; ++j) {
                   // use rand() for random integral value
                   remainder = rand() % 4; // equals to 0/1/2/3
                   if(remainder == 0){this->grid[i][j] = '.';}
                   else if (remainder == 1){this->grid[i][j] = 'S';}
                   else if (remainder == 2){this->grid[i][j] = 'W';}
                   else if (remainder == 3){this->grid[i][j] = 'F';}                   
                   } // inner for 
             } // for
     
     } // randomGrid





/*Every cell interacts with its eight neighbors, which are the cells that are 
horizontally, vertically, or diagonally adjacent. 
Check their nerghbors and update the number of count.
*/
void Game::updateCounter(int num1, int num2){
     this->emptyNum = 0; this->sheepNum= 0;
     this->wolfNum= 0; this->farmerNum= 0;
     
     // check the left/right and up/down of the current cell. Index: -1/0/1
     int leftRight, upDown;
     for(leftRight = -1; leftRight <= 1; ++leftRight) {
        for(upDown = -1; upDown <= 1; ++upDown) {
           // except the case of staying at the current cell with no changing position
           if(leftRight != 0 || upDown != 0) {
              // the position cannot be outside of the grid
              if( (leftRight + num1) >= 0 && (leftRight + num1) < this->row && 
                  (upDown + num2) >= 0 && (upDown + num2) < this->column) {
                  if(this->grid[leftRight + num1][upDown + num2] == '.') {this->emptyNum++;}
                  else if(this->grid[leftRight + num1][upDown + num2] == 'S') {this->sheepNum++;}
                  else if(this->grid[leftRight + num1][upDown + num2] == 'W') {this->wolfNum++;}
                  else if(this->grid[leftRight + num1][upDown + num2] == 'F') {this->farmerNum++;}
                  } // if - grid range
              } // if - 0
           
           } // inner for
        } // outer for
          
     }// updateCounter 
     
     
     
     
     
// Perform a transition according to the rules for each time step.
void Game::checkRules() {
     srand((unsigned)time(NULL));
     int i, j;
     int moveLocation = 0;
     int pickThisCell = 0;
     // looping through every single cell
     for(i = 0; i < this->row; ++i) {
             for(j = 0; j < this->column; ++j) {
                // check the neighbors and counts around this cell    
                updateCounter(i, j);
                
                /* If a cell is empty and surrounded by exactly two neighbors of
                 the same species, it is modified to contain a new instance of 
                 that species (reproduction). If a cell has two neighbors of more 
                 than one species, then the order in which they should be 
                 considered is sheep, wolf, and finally farmer.*/ 
                if(this->grid[i][j] == '.'){
                   if(this->sheepNum == 2){this->grid[i][j] = 'S';}
                   else if(this->wolfNum == 2){this->grid[i][j] = 'W';}
                   else if(this->farmerNum == 2){this->grid[i][j] = 'F';}
                   } // if - empty
                   
                /* If a cell contains a sheep and is surrounded by more than 
                three sheep neighbors, the cell dies (becomes empty) by 
                overpopulation. 
                If a cell contains a sheep and has at least one wolf as neighbor, 
                the cell dies (becomes empty) by predation.*/
                else if(this->grid[i][j] == 'S'){
                     if(this->sheepNum > 3){this->grid[i][j] = '.';}
                     if(this->wolfNum >= 1){this->grid[i][j] = '.';}                     
                     } // if - sheep
                
                /* if a cell contains a wolf and has more than three wolf 
                neighbors, it becomes empty.
                If a cell contains a wolf and has at least one neighbor who is 
                a farmer, the cell dies (becomes empty).
                If a cell contains a wolf and has only wolf and empty neighbors, 
                the cell dies becomes empty) due to starvation.*/
                else if(this->grid[i][j] == 'W'){
                     if(this->wolfNum > 3){this->grid[i][j] = '.';}
                     if(this->farmerNum >= 1){this->grid[i][j] = '.';}
                     if(this->sheepNum == 0){this->grid[i][j] = '.';}                     
                     } // if - wolf
                     
                /* If a cell contains a farmer and has at least one empty 
                neighbor cell, it moves to a randomly selected empty neighbor 
                cell. If there is no empty neighbor cell, the farmer cell 
                remains the same.*/     
                else if(this->grid[i][j] == 'F'){
                     if(this->emptyNum >= 1){
                        moveLocation = rand() % (this->emptyNum + 1);
                        pickThisCell = 0;
                               
                         int leftRight, upDown;
                         for(leftRight = -1; leftRight <= 1; ++leftRight) {
                            for(upDown = -1; upDown <= 1; ++upDown) {
                               // except the case of staying at the current cell with no changing position
                               if(leftRight != 0 || upDown != 0) {
                                  // the position cannot be outside of the grid
                                  if( (leftRight + i) >= 0 && (leftRight + i) < this->row && 
                                      (upDown + j) >= 0 && (upDown + j) < this->column) {
                                      if(this->grid[leftRight + i][upDown + j] == '.') {
                                         if(moveLocation == pickThisCell){
                                            this->grid[leftRight + i][upDown + j] = 'F';
                                            this->grid[i][j] = '.';}
                                            ++pickThisCell;}
                                      
                                      } // if - grid range
                                  } // if - 0
                               
                               } // inner for
                            } // outer for
                        
                                    
                        
                        } // if - emptyNum
                     } // if - farmer            
                } // inner for 
             } // for
     
     } // checkRules






// display the grid
void Game::display() {
     int i, j;
     for(i = 0; i < this->row; ++i) {
           for(j = 0; j < this->column; ++j) {
                 cout << this->grid[i][j];                  
                 } // inner for 
                 cout << endl;  
             } // for 
     } // display

















