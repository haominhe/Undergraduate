CXX =g++
CXXFLAGS = -g -std=c++11

all: main

%o : %.cpp game.hpp

GAME_OBJECTS = main.o game.o
main: $(GAME_OBJECTS)
	$(CXX) -o $@ $(GAME_OBJECTS) 
	
clean:
	$(RM) *.o main
