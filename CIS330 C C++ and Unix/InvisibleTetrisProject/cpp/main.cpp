//Invisible Tetris ,Winter 2016, CIS 330 Final Project
//Team name: This->
// By Haomin He, Yanting Liu and Guangyun Hou

#include "cpp/gameManager.h"
#include "cpp/menu.h"

int main() 
{
	//initializing game object, then jump to menu
    GameManager game;
    game.change_mode(MenuMode::Instance());
    game.execute();
}
