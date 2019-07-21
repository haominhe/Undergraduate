//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#include "cpp/pieces.h"
#include "cpp/board.h"

Board::Board() 
{
    //initialize score to 0
    score = 0;

    // flag of rendering score
    scoreRendering = true;
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLUMNS; j++)
        {   
            //assign every cell to -1, which means no color
            blockColor[i][j] = -1;
        }
    }
}

// bool function to check every row
bool Board::checkRow(int row) 
{
    //go through every column of the row
    for (int col = 0; col < COLUMNS; col++)
    {
        // if any cell is -1, it is empty(no color), so return false
        if (blockColor[row][col] == -1)  
        {    
            return false;
        }
    }
    return true;
}

// the row is full, the previous row should shift down
void Board::rowShiftDown(int i) 
{
    for (int row = i; row > 0; row--)
    {
        for (int col = 0; col < COLUMNS; col++)
        {
            blockColor[row][col] = blockColor[row-1][col];
        }
    }
}

//when eliminate row, add scores
void Board::eliminateRows()
{
    // keep tracking how many bonus points to be aded, the point is based on how many consecutive rows to be deleted
    int bonusPtAdd = 0; 
    level = 0;
    //check every single row from the bottom
    for (int row = ROWS-1; row >=0; row--) 
    {
        // if the cell is empy, jump to the end of the loop body
        if (!checkRow(row))
            continue;

        //if all cells in the row is not empty, shift the rown
        rowShiftDown(row);
        row++;

        // add level (+1)
        incrementLevel(1);

        //add the base score
        incrementScore(BASE);
        // cout how many times the score has been updated
        bonusPtAdd++;
        scoreRendering = true;
        levelRendering = true;
    }

    // if delete 4 rows at the same time, add bonous point
    if (bonusPtAdd == 4)
    {
       incrementScore(BONUS);
    }

}
// when a piece hits the bottom, add new piece
bool Board::addPieces(Pieces *piece) 
{
    for (int i = 0; i < piece->SIZE; i++) {
        int x = piece->xGetter(i);
        int y = piece->yGetter(i);

        // Tetromino isn't added to the board if it touches the upper border.
        if (y <= 0)
            return false;
        else
            // Add tetromino: update color in corresponding board block.
            blockColor[y][x] = piece->type;
    }
    return true;
}