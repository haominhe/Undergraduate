//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#include "cpp/pieces.h"
#include "cpp/board.h"

const int Pieces::block_list    [7][4][2]=
{   
    // I -type

    //  []
    //  []
    //  []
    //  []

    {
        {0,-1},     
        {0,0},
        {0,1},
        {0,2}
    },

    // z type
    //  [][]
    //    [][]
    {
        {0,-1},
        {0,0},
        {-1,0},
        {-1,1}
    },

    // square
    //  [][]
    //  [][]
    {
        {0,0},
        {0,1},
        {1,0},
        {1,1}
    },

    // s type
    //   [][]
    // [][]
    {
        {0,-1},
        {0,0},
        {1,0},
        {1,1}
    },

    // L type
    //  []
    //  []
    //  [][]
    {
        {-1,-1},
        {0,-1},
        {0,0},
        {0,1}
    },

    // J type
    //   []
    //   []
    // [][]
    {
        {1,-1},
        {0,-1},
        {0,0},
        {0,1}
    },

    // T type
    //  [][][]
    //    []
    {
        {0,0},
        {0,1},
        {0,2},
        {1,1}
    }
};

Pieces::Pieces(int new_type) {
    type = new_type;
    free_fall = false;
    faster = false;
    status = INACTIVE;
    movement = NONE;
    coords = new int[4][2];

    for (int i = 0; i < 4 ; i++) {
        coords[i][0] = block_list[type][i][0];
        coords[i][1] = block_list[type][i][1];
    }
}

void Pieces::rotate_left() {
    for (int i = 0; i < SIZE; i++) {
        int temp = coords[i][0];
        coords[i][0] = -coords[i][1];
        coords[i][1] = temp;
    }
}

void Pieces::rotate_right() {
    for (int i = 0; i < SIZE; i++) {
        int temp = coords[i][0];
        coords[i][0] = coords[i][1];
        coords[i][1] = -temp;
    }
}

void Pieces::get_shadow(Board *board, int shadow_y[]) {
    // Preserve tetromino state.
    int temp_y = y;
    Status temp_status = status;

    while (!has_landed()) {
        for (int i = 0; i < SIZE; i++)
            // Lands on tetromino or bottom of the board.
            if (xGetter(i) == board->ROWS ||
                    board->blockColor[yGetter(i)][xGetter(i)] != -1) {
                lands();
                y--;
                break;
            }
        if (!has_landed())
            y++;
    }

    // Save the position.
    for (int i = 0; i < SIZE; i++)
        shadow_y[i] = yGetter(i);

    // Return tetromino to initial state.
    y = temp_y;
    status = temp_status;
}