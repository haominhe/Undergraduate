# Project 1: Warmup
# Haomin He

# 1. hello
"""This program prints the greeting, 'hello, world', for a
    language in the terminal window.
    If there is nothing else on the command line besides the name
    of the program the greeting should be printed in English.
    This program can handle the situation where a language is not
    in the list of languages.
"""

from sys import argv

def hello():
    """ This function can print the greeting, 'hello, world', in five
    different languages.
    
    Args:
         None
    Returns:
         None
    """
    
    hellos = {'french':'Bonjour tout le monde', 'chinese':'你好,世界',
              'english': 'Hello, world', 'dutch':'Hallo, wereld',
              'russian':'Привет, мир'}
    if len(argv) == 1:
        print('Hello, world')
    elif argv[1] in hellos:
        print(hellos[argv[1]])
    else:
        print("Sorry, I don't speak " + argv[1].capitalize())


if __name__ == "__main__":
    hello()

