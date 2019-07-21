//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#include "cpp/gameManager.h"
#include "cpp/gameMode.h"
#define WIDTH 540 //define window size
#define HEIGHT 630

GameManager::GameManager() {
    //initialize everything
    SDL_Init(SDL_INIT_EVERYTHING);

    // Window and renderer.
    window = SDL_CreateWindow("INVISIBLE",SDL_WINDOWPOS_UNDEFINED,SDL_WINDOWPOS_UNDEFINED,WIDTH,HEIGHT,SDL_WINDOW_SHOWN|SDL_WINDOW_BORDERLESS);
    renderer = SDL_CreateRenderer(window,-1,SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    exit = false;
}

void GameManager::destroy() {
    // destroy the mode
    while (!modes.empty()) {
        modes.back()->destroy(this);
        modes.pop_back();
    }

    SDL_Quit();
}

void GameManager::execute() 
{
    while (!exit) {
        input(); // get input
        update(); // update the game
        render(); // render to screen
    }
    destroy();
}

void GameManager::change_mode(GameMode* mode) {
    // Clean up the current state.
    if (!modes.empty()) {
        modes.back()->destroy(this);
        modes.pop_back();
    }

    // Store and initialize the new state.
    modes.push_back(mode);
    modes.back()->init(this);
}

void GameManager::push_mode(GameMode* mode) {
    // Pause current state.
    if ( !modes.empty() )
        modes.back()->pause();

    // Store and initialize the new state.
    modes.push_back(mode);
    modes.back()->init(this);
}

void GameManager::pop_mode() {
    // Clean up the current state.
    if ( !modes.empty() ) {
        modes.back()->destroy(this);
        modes.pop_back();
    }

    // Resume previous state.
    if ( !modes.empty() )
        modes.back()->resume();
}


void GameManager::input() {
    // Let the state handle events.
    modes.back()->input(this);
}

void GameManager::update() {
    // Let the state update the game.
    modes.back()->update(this);
}

void GameManager::render() {
    // Let the state draw the screen.
    modes.back()->render(this);
}