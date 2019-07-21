//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#ifndef _BOARD_H_
#define _BOARD_H_

class Board 
{
    public:
        Board();
        
        static const int HEIGHT = 600;
        static const int WIDTH  = 300;
        static const int ROWS = 30;
        static const int COLUMNS = 15;
        static const int BLOCK_HEIGHT = HEIGHT / ROWS;
        static const int BLOCK_WIDTH = WIDTH / COLUMNS;
        static const int BONUS = 500;
        const int BASE = 100;
        int blockColor[ROWS][COLUMNS];
        bool scoreRendering;
        bool levelRendering;

        void incrementScore(int pointThisTime) {score += pointThisTime;}
        void incrementLevel(int lvThisTime) {level += lvThisTime;}
        int scoreGetter() {return score;}
        void eliminateRows();
        bool addPieces(Pieces* pieces);

 private:
        bool checkRow(int thisRow);
        void rowShiftDown(int thisRow);
        int score;
        int level;
};

#endif  // SRC_BOARD_H_