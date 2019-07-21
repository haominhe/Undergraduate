//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
//By Haomin He, Yanting Liu and Guangyun Hou
#include <random>
#include "cpp/playMode.h"
#include "cpp/gameManager.h"
#include "cpp/pieces.h"
#include "cpp/board.h"
#include "cpp/utilities.h"
#define  OPTIONCOLOR {255, 255, 255}
#define FONTPATH "resources/fonts/KM.otf"
#define SECOND 1200.0
using namespace std;

// static variable, bascially the mode
PlayMode PlayMode::m_playmode;

//function to initialize
void PlayMode::init(GameManager* game) 
{

    // Game objects.
    board        = new Board();
    piece        = new Pieces(rand()%7);       // Current tetromino.
    next_piece  = new Pieces(rand()%7);       // Next tetromino.

    // Texture of block
    block_texture = load_texture("resources/images/color.png", game->renderer);
    bottom_texture = load_texture("resources/images/tr.png",game->renderer);
    bg = load_texture("resources/images/bg.png",game->renderer);
    // Fonts texture and options
    TTF_Init();

    font_pause = TTF_OpenFont(FONTPATH, 30);
    font_tetris = TTF_OpenFont(FONTPATH, 20);
    font_score_text = TTF_OpenFont(FONTPATH, 18);
    font_score = TTF_OpenFont(FONTPATH, 22);
    font_game_over = TTF_OpenFont(FONTPATH, 30);

    image_pause = render_text("PAUSE",OPTIONCOLOR, font_pause, game->renderer);
    image_tetris = render_text("INVISIBLE",OPTIONCOLOR, font_tetris, game->renderer);
    image_score_text = render_text("SCORE:   ",OPTIONCOLOR, font_score_text, game->renderer);
    image_score = render_text(to_string(board->scoreGetter()),OPTIONCOLOR, font_score, game->renderer);
    image_game_over = render_text("GAME OVER!",OPTIONCOLOR, font_game_over, game->renderer);

    // Frame rate.
    acceleration    = 0.0008f;
    this_time       = 0;
    last_time       = 0;
    falling_time  = 0.5f;
    counter    = 0.0f;

    // Buttons coordinates.
    positionX1       = OFFSET+board->WIDTH+board->BLOCK_WIDTH;
    positionX2      = OFFSET+board->WIDTH+8*board->BLOCK_WIDTH;
    positionY1      = board->HEIGHT-4*board->BLOCK_HEIGHT;
    positionY2      = board->HEIGHT-6*board->BLOCK_HEIGHT;

    paused          = false;
    game_over       = false;
    exit            = false;

    // At the start of the game:
    // x position of (0, 0) block of tetro is columns/2
    // which is the exact horizontal middle of board.
    // y position of (0, 0) block of tetro is 0 which is the top of the board.
    piece->positionSetter(static_cast<int>(board->COLUMNS/2), 0);

    // Position next_tetro at the upper right of the window,
    // outside of the board.
    next_piece->positionSetter(board->COLUMNS+5, static_cast<int>(0.3*board->ROWS));
}

//function to clean up when closed
void PlayMode::destroy(GameManager* game) 
{

    TTF_CloseFont(font_pause);
    TTF_CloseFont(font_tetris);
    TTF_CloseFont(font_score_text);
    TTF_CloseFont(font_score);
    TTF_CloseFont(font_game_over);

    SDL_DestroyTexture(block_texture);
    SDL_DestroyTexture(bottom_texture);
    SDL_DestroyTexture(bg);
    SDL_DestroyTexture(image_pause);
    SDL_DestroyTexture(image_tetris);
    SDL_DestroyTexture(image_score_text);
    SDL_DestroyTexture(image_score);
    SDL_DestroyTexture(image_game_over);

    IMG_Quit();
    SDL_DestroyRenderer(game->renderer);
    SDL_DestroyWindow(game->window);
    SDL_Quit();
}

// Render result.
void PlayMode::render(GameManager* game) {
    // Clear screen.
    SDL_SetRenderDrawColor(game->renderer, 0, 0, 0, 1);
    SDL_RenderClear(game->renderer);

    render_texture(bg,game->renderer,0,0);
    // Render "Tetris" text.
    int x = (next_piece->x-3)*board->BLOCK_WIDTH;
    int y = OFFSET;

    // Render score.
    if (board->scoreRendering) 
    {
        image_score = render_text(to_string(board->scoreGetter()),OPTIONCOLOR, font_score, game->renderer);
        board->scoreRendering = false;
    }
    render_texture(image_score,game->renderer, x + 60, y + board->BLOCK_WIDTH);

    render_texture(image_tetris, game->renderer, x, y);
    // Render "Pause" text if game is paused.
    if (paused)
    {
        render_texture(image_pause, game->renderer, x, y+40);
    }

    // Render score text.
    render_texture(image_score_text,
            game->renderer, x, y + board->BLOCK_WIDTH);

    int piece_x, piece_y;
    
    SDL_Rect clips[7];
    for (int i = 0; i < 7; i++) 
    {
        clips[i].x = 0;
        clips[i].y = i*24;
        clips[i].w = 20;
        clips[i].h = 20;
    }

        // Special case for square
    for (int i = 0; i < piece->SIZE; i++) 
    {
        // Get new coordinates.
        piece_x = piece->xGetter(i)*board->BLOCK_WIDTH + OFFSET;
        piece_y = piece->yGetter(i)*board->BLOCK_HEIGHT + OFFSET;

        draw_block(game, piece_x, piece_y, piece->type, clips);
    }


    // if the game is continuting
    if (!game_over) 
    {
        // Draw next tetromino.
        for (int i = 0; i < next_piece->SIZE; i++) 
        {
            // Get new coordinates.
            piece_x = next_piece->xGetter(i)*board->BLOCK_WIDTH;
            piece_y = next_piece->yGetter(i)*board->BLOCK_HEIGHT;
            //render the normal blocks
            draw_block(game, piece_x, piece_y, next_piece->type, clips);
        }
    }

    // This is the board. Non-active tetrominos live here.
    for (int i = 0; i < board->ROWS; i++)
    {
        for (int j = 0; j < board->COLUMNS; j++)
        {
            if (board->blockColor[i][j] != -1) 
            {
                // Get new coordinates.
                piece_x = j*board->BLOCK_WIDTH + OFFSET;
                piece_y = i*board->BLOCK_HEIGHT + OFFSET;

                draw_invisible(game, piece_x, piece_y, board->blockColor[i][j], clips);
            }
        }
    }
    // If game is over, display "Game Over!".
    if (game_over)
        render_texture(image_game_over,
                game->renderer, positionX1,
                game->height-positionY1+4*board->BLOCK_WIDTH);

    // Swap buffers.
    SDL_RenderPresent(game->renderer);
}

// pause function, activate pause
void PlayMode::pause() 
{
    paused = true;
}

void PlayMode::resume() 
{
    paused = false;
}

// function to restart the game.
void PlayMode::reset() 
{
    // to empty the current board
    for (int i = 0; i < board->ROWS; i++) {
        for (int j = 0; j < board->COLUMNS; j++) {
            board->blockColor[i][j] = -1;
        }
    }

    // Delete objects (previous game)
    delete [] board;
    delete [] piece;
    delete [] next_piece;

    // create new objects.
    board = new Board();
    piece = new Pieces(rand()%7);
    next_piece = new Pieces(rand()%7);
    piece->positionSetter(static_cast<int>(board->COLUMNS/2), 0);
    next_piece->positionSetter(board->COLUMNS+5, static_cast<int>(0.3*board->ROWS));

    game_over       = false;

    paused = false;
}
// Render blocks.
void PlayMode::draw_block(GameManager* game,
        int x, int y, int k, SDL_Rect clips[]) {
    render_texture(block_texture, game->renderer, x, y, &clips[k]);
}

//function to load invisible block to the screen
void PlayMode::draw_invisible(GameManager* game,
        int x, int y, int k, SDL_Rect clips[]) {
    render_texture(bottom_texture, game->renderer, x, y, &clips[k]);
}

//frame rate function
float PlayMode::frame_rate(GameManager* game, int* last_time, int* this_time) {
    // Get number of milliseconds since SDL_Init() of the previous frame.
    *last_time = *this_time;

    // Get number of milliseconds since SDL_Init().
    *this_time = SDL_GetTicks();

    return ((*this_time - *last_time) /SECOND);
}

// Handle player input.
void PlayMode::input(GameManager *game) 
{
    // Queuing events.
    SDL_Event event;
    while (SDL_PollEvent(&event)) 
    {
        // Clicking 'x' 
        if (event.type == SDL_QUIT) 
        {
            exit = true;
        }

        // Key is pressed.
        if (event.type == SDL_KEYDOWN) 
        {
            // Pause/Resume.
            if (event.key.keysym.sym == SDLK_p) 
            {
                if (paused) {
                    resume();
                } else {
                    pause();
                }
            }

            if (!paused && !piece->free_fall) 
            {
                switch (event.key.keysym.sym) 
                {
                    case SDLK_ESCAPE:
                        exit = true;
                        break;
                    case SDLK_a: case SDLK_LEFT:
                        piece->movement = piece->LEFT;
                        piece->shift = true;
                        break;
                    case SDLK_d: case SDLK_RIGHT:
                        piece->movement = piece->RIGHT;
                        piece->shift = true;
                        break;
                    case SDLK_w: case SDLK_UP:
                            piece->rotate = true;
                        break;
                    case SDLK_s: case SDLK_DOWN:
                        piece->faster = true;
                        break;
                    case SDLK_SPACE:
                        piece->free_fall = true;
                        break;
                    default:
                        break;
                }
            }
        }

        // Key is released.
        if (event.type == SDL_KEYUP) 
        {
            switch (event.key.keysym.sym) {
                case SDLK_s: case SDLK_DOWN:
                    piece->faster = false;
                    break;
                default:
                    break;
            }
        }
    }
}

void PlayMode::release_tetromino() 
{
    Pieces* new_piece = new Pieces(rand()%7);
    new_piece->positionSetter(next_piece->x, next_piece->y);

    delete[] piece;
    piece = next_piece;
    piece->positionSetter(static_cast<int>(board->COLUMNS/2), 0);

    next_piece = new_piece;

    piece->drop();
}

// Update game values.
void PlayMode::update(GameManager* game) {

    //x , esc was pressed
    if (exit) {
        game->quit();
    }

    if (game_over || paused) {
        return;
    }

    // Tetromino has landed.
    if (piece->has_landed()) {
        piece->free_fall = false;

        // Add fallen tetromino to the board and check if tetromino.
        // has crossed over the top border.
        if (!board->addPieces(piece)) {
            game_over = true;
            return;
        }

        // Drop stored tetromino and replace by newly-generated tetromino.
        release_tetromino();
    } else if (piece->free_fall) {
        piece->y++;  // Maximum speed.
    } else {  // Rotations and translations.
        // Rotation.
        if (piece->rotate)
            piece->rotate_left();

        // Update tetromino position on the x-axis.
        piece->add_to_x(piece->movement);

        // Assign the time required for tetromino to fall down one block.
        if (piece->faster) {
            falling_time = 0.02f;  // 2x slower than free fall.
        } else {
            // Drop speed proportional to score.
            falling_time = 0.3f - board->scoreGetter()*acceleration;
        }

        // Add time elapsed.
        counter += frame_rate(game, &last_time, &this_time);

        // time_till_drop = 0.3;
        // delta_time ~ 0.017 seconds.
        // Tetromino initially falls one block unit for
        // every 0.3/0.017 ~ 17 game loops.

        if (counter >= falling_time) {
            piece->y++;  // Update tetromino position on the y-axis.
            counter = 0.0f;
        }
    }

    // Collision detection.
    // Check if tetromino is in an acceptable position,
    // if not, undo previous move(s).
    for (int i = 0; i < piece->SIZE; i++) {
        // Coordinates of each block.
        int x = piece->xGetter(i);
        int y = piece->yGetter(i);

        // Block crosses wall after rotation and/or translation.
        if (x < 0 || x >= board->COLUMNS) {
            // Because of rotation.
            if (piece->rotate)
                piece->rotate_right();  // Neutralize the left rotation.

            // Because of translation.
            if (piece->shift)
                piece->x -= piece->movement;  // Neutralize shift.

            break;
        } else if (y >= board->ROWS) {  // Block touches ground.
            piece->lands();
            // Change the value of Y so that block(s) of the (old)
            // tetromino is/are above the blue line.
            piece->ySetter(i, board->ROWS-1);
        } else if (y >= 0) {  // Block is on the board.
            // Block touched another block.
            if (board->blockColor[y][x] != -1) {
                // Tetromino rotates and collides with a block.
                if (piece->rotate || piece->shift) {
                    if (piece->rotate) {
                        piece->rotate_right();  // Neutralize.
                    }
                    // Tetromino is shifted into another block.
                    if (piece->shift) {
                        piece->x -= piece->movement;  // Neutralize.
                    }
                    break;
                } else {  // Block falls into another block.
                    piece->y--;  // Neutralize: tetromino goes up.
                    piece->lands();
                }
            }
        }
    }
    board->eliminateRows();
    piece->rotate = false;
    piece->shift = false;
    piece->movement = piece->NONE;
}