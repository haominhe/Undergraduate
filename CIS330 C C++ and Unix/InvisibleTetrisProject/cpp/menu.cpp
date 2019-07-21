//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#include "cpp/menu.h"
#include "cpp/playMode.h"
#include "cpp/utilities.h"
#define POSITIONX 240
#define POSITIONY 320
#define GAP 35
#define FONTPATH "resources/fonts/KM.otf"
#define FONTSIZE 28

MenuMode MenuMode::m_menumode;

// function to initialize all the nccessary stuff
void MenuMode::init(GameManager* game) 
{
    play = false;
    exit = false;
    OPTIONCOLOR =  {255,255,255};
    HIGHLIGHTCOLOR = {0,0,0};
    // Initialize fonts and font color.
    TTF_Init();

    // Load fonts and font textures.
    title_image = load_texture("resources/images/title.png", game->renderer);
    font_play = TTF_OpenFont(FONTPATH, FONTSIZE);
    font_quit = TTF_OpenFont(FONTPATH, FONTSIZE);
    play_image = render_text("Play", OPTIONCOLOR, font_play, game->renderer);
    quit_image = render_text("Quit", OPTIONCOLOR, font_quit, game->renderer);

    current = 0;
    choices = 2;
}

void MenuMode::destroy(GameManager* game) 
{
    // Close all fonts.
    TTF_CloseFont(font_play);
    TTF_CloseFont(font_quit);

    // Destroy all textures.
    SDL_DestroyTexture(title_image);
    SDL_DestroyTexture(play_image);
    SDL_DestroyTexture(quit_image);

    IMG_Quit();
}

void MenuMode::render(GameManager* game) 
{
    // set background color
    SDL_SetRenderDrawColor(game->renderer, 255, 64, 128, 1);
    SDL_RenderClear(game->renderer);

    //render title image
    render_texture(title_image, game->renderer,0,0);

    if (current== 0) 
    {
        play_image = render_text("Play",HIGHLIGHTCOLOR, font_play, game->renderer);
    } 
    else if (current== 1) 
    {
        quit_image = render_text("Quit", HIGHLIGHTCOLOR, font_quit, game->renderer);
    }

    // Draw menu items (centered).
    render_texture(play_image, game->renderer,POSITIONX,POSITIONY);
    render_texture(quit_image, game->renderer,POSITIONX,POSITIONY+GAP);

    // Remove underline again.
    if (current== 0) 
    {
        play_image = render_text("Play", OPTIONCOLOR, font_play, game->renderer);
    }

    else if (current== 1) 
    {
        quit_image = render_text("Quit", OPTIONCOLOR, font_quit, game->renderer);
    }

    // Swap buffers.
    SDL_RenderPresent(game->renderer);
}

void MenuMode::pause() {}

void MenuMode::resume() {}

void MenuMode::reset() {}

void MenuMode::input(GameManager* game) {
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        // Clicking 'x' or pressing F4.
        if (event.type == SDL_QUIT)  {
            exit = true;
        }

        // Key is pressed.
        if (event.type == SDL_KEYDOWN) 
        {
            switch (event.key.keysym.sym) 
            {
                case SDLK_ESCAPE:
                    exit = true;
                    break;
                case SDLK_UP:
                    move_up();
                    break;
                case SDLK_DOWN:
                    move_down();
                    break;
                case SDLK_RETURN:
                    if (current == 0)
                        play = true;
                    else if (current== 1)
                        exit = true;
                    break;
                default:
                    break;
            }
        }
    }
}

//if play, update, else exit
void MenuMode::update(GameManager* game)
{
    if (play) 
    {
        game->push_mode(PlayMode::Instance());
    } 
    else if (exit) 
    {
        game->quit();
    }
}

// move up arrow
void MenuMode::move_up()
{
    if (current > 0) 
    {
        current= (current-1)%choices;
    }
}

//move down arrow
void MenuMode::move_down() 
{
    if (current < choices-1) 
    {
        current= (current+1)%choices;
    }
}
