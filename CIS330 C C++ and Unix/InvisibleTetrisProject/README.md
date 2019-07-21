# Final Project - Invisible Tetris
Winter 2016, CIS 399

Team Name: This->

Name: Haomin He, Yanting Liu, Guangyun Hou

A tetris project for CIS 399 

## Declaration Statement
* This project is created and modified based on the software of 21st-century-tetris (Original Author: chaficnajjar) on Github. What we did to the code, and usage, all behavior are under The MIT license. The original 21st-century-tetris, all copyright to the original author. For the original license and other resources learned and SDL setup for this project, see the last 2 parts of this README document.

## Setup Instruction

* MacOX:

	Using terminal to get in the Invisible Tetris directory (InvisibleTetris folder), simply use 'make' command, the makefile will compile the cpp and h files automatically, then run the INVISIBLE program to start the Game.

* Linux:
	Same as MacOX instruction.

* Windows:
	Not supported yet.

## Play Instruction

Up arrow -> rotates the current tetromino

Left arrow -> moves the current tetromino to the left

Right arrow -> moves the current tetromino to the right

Down arrow -> speeds up the current tetromino

Spacebar -> drop the current tetromino immediately 

p -> pauses/resumes game

When the game is over, use ESC to exit. If you want to play again, you have to start opening the program again.

## Improvement and Changes compare to original tetris
* Made the UI better, used SDL images instead of simply rendering

* Added the function to let the block became invisible

* Not using music engine anymore

* Fixed the tetromino bugs (droping over the board) in original

## Code, Idea, and other references

https://github.com/chaficnajjar/21st-century-tetris

Also, the usage of SDL2, and other tetris logic and codes from the resources of the following:

https://en.wikipedia.org/wiki/Tetris

http://www.tetrisfriends.com/games/

http://www.tetrisfriends.com/games/Marathon/game.php

http://zetcode.com/tutorials/javagamestutorial/tetris/

http://aaroncox.net/tutorials/arcade/tetris.pdf

http://pygame.org/project-Tetris+in+73+Lines-800-.html

http://codeincomplete.com/posts/2011/10/10/javascript_tetris/

http://superliminal.com/tetris/Tetris.java

http://mrcoles.com/tetris/#random

http://noobtuts.com/unity/2d-tetris-game

https://www.youtube.com/watch?v=htfB7D2ruXw&feature=share

https://www.youtube.com/watch?v=X91_x7ReYyM

https://www.youtube.com/watch?v=ZNouGfMHPQg

https://www.youtube.com/watch?v=T30_Tt8aCOE

http://www.freetetris.org/index.html

http://www.freetetris.org/game.php

https://github.com/bluesky466/Tetris

https://github.com/PSNB92/Tetris

https://github.com/DQNEO/CppTetris

https://github.com/mattbierner/Super-Template-Tetris

https://github.com/tdd-elevator-training/tetris

https://www.khanacademy.org/computer-programming/tetris/1782938813

http://gamedevelopment.tutsplus.com/tutorials/implementing-tetris-collision-detection--gamedev-852

http://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/

## Original Author and Tetris version:
* link: https://github.com/chaficnajjar/21st-century-tetris

* Here is the license for the original version:

The MIT License (MIT)

Copyright (c) 2014 Chafic Najjar

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

