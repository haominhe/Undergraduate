CPPFLAGS		+= $(SDL_INCLUDE)
CXXFLAGS		+= $(DEBUG) -Wall -std=c++11
LDFLAGS			+= $(SDL_LIB)

DEBUG			:= -g

SDL_INCLUDE		:= `sdl2-config --cflags` -I.
SDL_LIB			:= `sdl2-config --libs` -lSDL2_ttf -lSDL2_image 

BINARY 			:= INVISIBLE
SRCS			:= $(wildcard cpp/*.cpp)
OBJS			:= $(SRCS:.cpp=.o)

all: $(BINARY)

$(BINARY): $(OBJS)
	$(LINK.cc) $(OBJS) -o $(BINARY) $(LDFLAGS)

.depend: $(SRCS)
	@- $(RM) .depend
	@- $(CXX) $(CPPFLAGS) $(CXXFLAGS) -MM $^ | sed -r 's|^([^ ])|src/\1|' > .depend;

-include .depend

clean:
	@- $(RM) $(BINARY)
	@- $(RM) $(OBJS)
	@- $(RM) .depend