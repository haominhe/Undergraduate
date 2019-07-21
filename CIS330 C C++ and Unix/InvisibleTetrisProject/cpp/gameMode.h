//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#ifndef _GAMESTATE_H_
#define _GAMESTATE_H_

#include "cpp/gameManager.h"

//abstract class of game mode
class GameMode {
 public:
    virtual void init(GameManager* game) = 0;
    virtual void destroy(GameManager* game) = 0;

    virtual void pause() = 0;
    virtual void resume() = 0;

    virtual void input(GameManager* game) = 0;
    virtual void update(GameManager* game) = 0;
    virtual void render(GameManager* game) = 0;

    void change_mode(GameManager* game, GameMode* mode) {
        game->change_mode(mode);
    }

 protected:
    GameMode() { }
};

#endif  // SRC_GAMESTATE_H_
