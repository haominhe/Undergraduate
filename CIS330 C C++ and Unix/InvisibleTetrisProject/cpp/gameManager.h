//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#ifndef _GAMEMANAGER_H_
#define _GAMEMANAGER_H_

#include <SDL2/SDL.h>
#include <list>

class GameMode;

class GameManager {
 public:
    // size of window variable.
    int width;
    int height;

    // Window and renderer.
    SDL_Window* window;
    SDL_Renderer* renderer;


    // constructor
    GameManager();

    //function to clean up
    void destroy();

    //change current mode
    void change_mode(GameMode* mode);
    void push_mode(GameMode* mode);
    void pop_mode();

    void execute();
    void input();
    void update();
    void render();

    bool running() { return !exit; }
    void quit() { exit = true; }

 private:
    //define type of stack of mode
    typedef std::list<GameMode*> ModeStack;
    ModeStack modes;
    bool exit;
};

#endif  // SRC_GAMEMANAGER_H_