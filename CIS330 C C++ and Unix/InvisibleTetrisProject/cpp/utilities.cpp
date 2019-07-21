//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#include "cpp/utilities.h"

// the function to render texture, with anytype, and copy to renderer
void render_texture(SDL_Texture *tex,SDL_Renderer* ren, SDL_Rect dst, SDL_Rect* clip) 
{
    SDL_RenderCopy(ren, tex, clip, &dst);
}

// the function to get the texture
void render_texture(SDL_Texture* tex,SDL_Renderer *ren, int x, int y, SDL_Rect* clip) 
{
    SDL_Rect dst;
    dst.x = x;
    dst.y = y;
    if (clip != nullptr) {
        dst.w = clip->w;
        dst.h = clip->h;
    } else {
        SDL_QueryTexture(tex, nullptr, nullptr, &dst.w, &dst.h);
    }

    render_texture(tex, ren, dst, clip);
}

// the function to render text to texture
SDL_Texture* render_text(const std::string &message,
        SDL_Color color, TTF_Font* font, SDL_Renderer* renderer) 
{
    SDL_Surface* surf = TTF_RenderText_Blended(font, message.c_str(), color);

    SDL_Texture* texture = SDL_CreateTextureFromSurface(renderer, surf);

    SDL_FreeSurface(surf);
    return texture;
}

// function to load texture 
SDL_Texture* load_texture(const std::string &file, SDL_Renderer* ren) 
{
    SDL_Texture* texture = IMG_LoadTexture(ren, file.c_str());
    return texture;
}