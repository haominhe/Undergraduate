/* 
    Name: Haomin He
    DuckID: hhe6
    CIS415 Project1
    Fall 2016
    This is my own work.
    
    Resources: 
    CIS 415 Lab3 code
    c/c++ programming by examples - create a timer
    setitimer: Setting Interval Timers
    COMPILE AND EXECUTE C ONLINE
    pipes/simple_pipe.c
    The fork() System Call
    C - reading command line parameters
    How to select/read/copy values after specific character in a string
    Elapsed Time
    Linux manual page
    Signal Handling
*/



#include <sys/time.h>	/* for timeval */
#include <unistd.h>		/* for pause */
#include <stdio.h>		/* for printf */
#include <stdlib.h>		/* for exit */
#include <signal.h>		/* for signal */
#include <sys/wait.h>   /* for wait */
#include "p1fxns.h"     /* for helper functions */
#include <sys/types.h>
#include <sys/ptrace.h>
#include <string.h>
#define UNUSED __attribute__((unused))


/* 
The number of processes and processors is optional, since
thv? will look in the environment for environment variables named TH_NPROCESSES and
TH_NPROCESSORS, respectively, before processing the command line arguments. Thus, if
either or both of these environment variables are defined, then thv? takes the values from the
environment variable. If the corresponding argument is also specified, the argument overrides the
environment variable.
*/
#define TH_NPROCESSES 3
#define TH_NPROCESSORS 3
#define MAX_VALUE 1024
    
    
/*
Obtain the number of processes to create (nprocesses), the number of processors upon which
to run those programs (nprocessors), and the command to execute in each of the processes
(command) from the environment variables and command arguments to TH.
*/
//the number of processes, initialize 
int nprocesses = TH_NPROCESSES;
//the number of processors
int nprocessors = TH_NPROCESSORS;    



// to see if a string starts with a certain word, like "--number="
static int StartsWith(const char *a, const char *b)
{
    while(*b){
        if(*b++ == *a++){
            // do nothing if they are the same
        } else if (*b++ != *a++){
            // two strings are different
            return 0;
        }
    }
    // b string belongs to a string
    return 1;
}


int main(UNUSED int argc, UNUSED char* argv[]){
    // record the current time and end time
    struct timeval start, end;
    // gettimeofday takes timeval and timezone
    gettimeofday(&start, NULL);

    // set a buffer 
    char* buffer = (char*)malloc(sizeof(char) * MAX_VALUE);
    //the command
    char* command = NULL;
    

    // command line example handling: ./thv1 --command=ls  
    // # both environment variables must be set to 3 and exported

    // getenv searches for the environment string pointed to by 
    // name and returns the associated current value to the string
    char* temp1;
    char* temp2;
    temp1 = getenv("TH_NPROCESSES");
    temp2 = getenv("TH_NPROCESSORS");
    /*
    reset or insert the environment variable, if overwrite is zero the variable is not reset.
    If getenv returns NULL, the environment variable does not exist.
    */
    if(temp1 == NULL) {setenv("TH_NPROCESSES", "3", 0);}
    if(temp2 == NULL) {setenv("TH_NPROCESSORS", "3", 0);}

    temp1 = getenv("TH_NPROCESSES");
    temp2 = getenv("TH_NPROCESSORS");

    nprocesses = p1atoi(temp1);
    nprocessors = p1atoi(temp2);


    int ctr;
    char *pointnext;
    command = (char*)malloc(sizeof(char) * MAX_VALUE);
    //check command line arguement 
    if(argc >= 2 && argc <= 4) {
        // assess the second arguement at the beginning
        for(ctr = 1; ctr < argc; ctr++){
            if(StartsWith(argv[ctr], "--number=")) {nprocesses = p1atoi(argv[ctr] + p1strlen("--number="));}
            else if(StartsWith(argv[ctr], "--processors=")) {nprocessors = p1atoi(argv[ctr] + p1strlen("--processors="));}
            else if(StartsWith(argv[ctr], "--command=")) {               
                pointnext = strchr(argv[ctr], '=');
                // word after '=' sign
                pointnext++; 
                command = pointnext;
            } else {
                p1perror(1, "Error: Command line arguements are invalid");
                free(buffer);
                exit(1);
            }
        }// for loop
    } else {
        // failed command line arguement
        p1perror(1, "Error: Command line arguements are at least 2, at most 4");
        free(buffer);
        exit(1);
    }


    // get the command and parse it
    // base case
    int index;
    index = 0;
    char ** arglist = (char**)malloc(sizeof(char*) * 5);
    index = p1getword(command, index, buffer);
    arglist[0] = (char*)malloc(sizeof(char) * 50);
    p1strcpy(arglist[0], buffer);
    arglist[1] = NULL; // last element is null

    // inductive case
    buffer[0] = 0;
    ctr = 1;
    while(command[index] != '\0'){
        index = p1getword(command, index, buffer);
        arglist[ctr] = (char*)malloc(sizeof(char) * p1strlen(buffer)* 5);
        p1strcpy(arglist[ctr], buffer);
        arglist = (char**)realloc(arglist, sizeof(char*) * 50);
        arglist[ctr] = NULL; // last element is null
    }
    


	int i;
    pid_t* pid;
    pid = (pid_t*)malloc(sizeof(pid_t) * nprocesses);
    buffer[0] = 0;

	for(i = 0; i < nprocesses; i++){
        signal(SIGUSR1, NULL);
        pid[i] = fork();
		if(pid[i] < 0){
			fprintf(stderr, "Fork() failed to create child %d.\n", i);
            free(buffer);
            free(command);
            free(pid);
            int x = 0;
            while(arglist[x] != NULL){free(arglist[x++]);}
            free(arglist);
			exit(1);
		}
		else if(pid[i] > 0){
			//parent
            signal(SIGUSR1, SIG_IGN);
		}	
		else{
			pause();
			execvp("arglist[0]", arglist);
		}
	}
	//Parent should be only process executing past this point...
    signal(SIGUSR1, SIG_IGN);
    sleep(1);

    for( i = 0; i < nprocesses; i++){
        kill(pid[i], SIGUSR1);
    }    

	for( i = 0; i < nprocesses; i++){
		wait(&pid[i]);
	}



    gettimeofday(&end, NULL);
    buffer[0] = 0;
    p1putstr(1, "The elapsed time to execute ");
    p1itoa(nprocesses, buffer);
    p1putstr(1, buffer);
    p1putstr(1, " copies of \"");
    p1putstr(1, command);
    p1putstr(1, "\" on ");
    p1itoa(nprocessors, buffer);
    p1putstr(1, buffer);
    p1putstr(1, " processors is ");
    int seconds;
    seconds = ((end.tv_sec * 1000000 + end.tv_usec) - (start.tv_sec * 1000000 +start.tv_usec));
    p1itoa(seconds, buffer);
    p1putstr(1, buffer);
    p1putstr(1, " \n");

    free(buffer);
    free(command);
    free(pid);
    int x = 0;
    while(arglist[x] != NULL){free(arglist[x++]);}
    free(arglist);
    
	return 0;

}











    
