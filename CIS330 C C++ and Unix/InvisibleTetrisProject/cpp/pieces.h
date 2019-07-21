//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou
#ifndef _PIECES_H_
#define _PIECES_H_

class Board;

class Pieces 
{
 public:
    // Explicit Constructor. Do not want implicit conversions happening under the hood
    explicit Pieces(int type);

    
    /* enumeration is a distinct type whose value is restricted to a range of values 
    values of an integral type known as the underlying type of the enumeration 
    There are four types of conditons for each cells*/
    enum PresentCellCondition {DONE, NOTUSED, FALL, AWAIT};
    enum GoToDirection   {TOLEFT = -1, STAY = 0, TORIGHT = 1};



    enum Status {INACTIVE, WAITING, FALLING, LANDED};
    enum Movement {NONE = 0, LEFT = -1, RIGHT = 1};

    // size is not gonna be changed, so we are using constant
    static const int SIZE = 4;

    // seven types of shape, occupy four rows for each shape, two is the coordination/columns
    static const int block_list[7][4][2];
    Status status;
    Movement movement;
    int x;
    int y;
    int type;
    bool free_fall;  // True if spacebar was pressed, falls down.
  // True if 's' or 'down' was pressed, falls faster.
    bool faster;
    bool shift;  // True if player shifts tetromino left or right.
    bool rotate;  // True if rotation occured (always counterclockwise).
    int (*coords)[2];  // Relative coordinates (used for rotation).
    // Sets position of the block at (0, 0)
    void positionSetter(int new_x, int new_y) {x = new_x; y = new_y;}

    // Sets position of any block
    void xSetter(int i, int new_x) {x = new_x - coords[i][0];}
    void ySetter(int i, int new_y) {y = new_y - coords[i][1];}

    // Get x coordinate of upper left vertex of block i
    int xGetter(int i) {return x + coords[i][0];}

    // Get y coordinate of upper left vertex of block i
    int yGetter(int i) {return y + coords[i][1];}

    void add_to_x(int x_offset) { x += x_offset;}

    bool has_landed() {return status == LANDED;}
    void lands() {status = LANDED;}
    void drop() {status = FALLING;}

    void rotate_right();
    void rotate_left();

    void get_shadow(Board* board, int shadow_y[]);
};

#endif  // SRC_TETROMINO_H_
