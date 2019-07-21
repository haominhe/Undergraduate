//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#ifndef _PLAYMODE_H_
#define _PLAYMODE_H_
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <SDL2/SDL_image.h>
#include "cpp/gameMode.h"

class Pieces;
class Board;

class PlayMode : public GameMode {
 public:
    static const int NCOLORS = 7;

    // Space between board border and window border.
    static const int OFFSET = 20;

    void init(GameManager* game);
    void destroy(GameManager* game);

    void pause();
    void resume();
    void reset();

    void input(GameManager* game);
    void update(GameManager* game);
    void render(GameManager* game);

    static PlayMode* Instance() { return &m_playmode; }

 protected:
    PlayMode() { }

 private:
    static PlayMode m_playmode;

    // Frame rate.
    float acceleration;  // Multiplied by score to provide falling speed.
    int this_time;  // Time since SDL_Init() of the current game loop.
    int last_time;  // Time since SDL_Init() of the previous game loop.
    float falling_time;  // Tetromino falls down 1 block every
                           // time_till_drop seconds.
    float counter;  // Counts number of game loops to allow
                         // tetromino to fall down.

    // switch to passed the game
    bool paused;
    // switch to check if it's gameover
    bool game_over;
    // switch to exit  
    bool exit;
    
    // coordination.
    int positionX1;
    int positionX2;
    int positionY1;
    int positionY2;

    void release_tetromino();
    void draw_block(GameManager* game, int x, int y, int k, SDL_Rect clips[]);
    void draw_invisible(GameManager* game,int x, int y, int k, SDL_Rect clips[]); 
    void create_button(GameManager* game,int x, int y, int width, int height, int color[]);
    float frame_rate(GameManager* game, int *last_time, int *this_time);

    // Game objects.
    Board* board;
    Pieces* piece;
    Pieces* next_piece;

    // Fonts.
    TTF_Font*  font_pause;
    TTF_Font*  font_tetris;
    TTF_Font*  font_score_text;
    TTF_Font*  font_score;
    TTF_Font*  font_game_over;

    // Texture.
    SDL_Texture* block_texture;
    SDL_Texture* bottom_texture;
    SDL_Texture* bg;
    SDL_Texture* image_pause;
    SDL_Texture* image_tetris;
    SDL_Texture* image_score_text;
    SDL_Texture* image_score;
    SDL_Texture* image_game_over;

};

#endif  // SRC_PLAYMODE_H_
