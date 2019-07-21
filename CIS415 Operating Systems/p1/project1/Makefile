CC = gcc
CFLAGS = -W -Wall
SOURCE = thv1.c p1fxns.c
OBJECTS = ${SOURCE:.c=.o}
PROGS = thv1

all: $(PROGS)
#	$(CC) $(CFLAGS) -o $@ $^

thv1: thv1.o p1fxns.o
	$(CC) $(CFLAGS) -o thv1 thv1.o p1fxns.o


thv1.o: thv1.c p1fxns.h

p1fxns.o: p1fxns.c p1fxns.h

clean:
	rm $(PROGS) *.o
