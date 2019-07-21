//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou
#ifndef _MENU_H_
#define _MENU_H_

#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>

#include "cpp/gameMode.h"

class MenuMode : public GameMode {
 public:
    static MenuMode* Instance() { return &m_menumode; }
    
    // initlaization menu
    void init(GameManager* game);

    //destory the image if change status
    void destroy(GameManager* game);
    void initializeImages(GameManager* game);

    void pause();
    void resume();
    void reset();

    // function to receive input
    void input(GameManager* game);

    // function to update the status
    void update(GameManager* game);

    //function to render images to screen
    void render(GameManager* game);

    // operations for up or down in menu
    void move_up();
    void move_down();

 protected:
    MenuMode() { }

 private:
    static MenuMode m_menumode;

    //switches for play or exit
    bool play;
    bool exit;

    // Text position.
    int play_width, play_height;
    int quit_width, quit_height;

    // Currently selected menu item.
    int current;

    // Number of choices.
    int choices;

    // Font textures and colors
    SDL_Color       OPTIONCOLOR;
    SDL_Color       HIGHLIGHTCOLOR;
    TTF_Font*       font_play;
    TTF_Font*       font_quit;
    SDL_Texture*    title_image;
    SDL_Texture*    play_image;
    SDL_Texture*    quit_image;
};

#endif  // SRC_MENUMODE_H_
