/* 
	Name: Haomin He
	DuckID: hhe6
	CIS415 Project0
	Fall 2016
	This is my own work. 

	Resources: 
	Textbooks
	C standard library - tutorialspoint.com
	stackoverflow - Reading a text file into data structure in C
	Hashtable in C
	Compare integers in C
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mentry.h"

#define FULLNAMESIZE 1000
#define STRSIZE 2000
#define ZIPSIZE 3000



/*  Consturctor 
	me_get returns the next file entry from fd, or NULL if end of file 
	Use malloc() to allocate the MEntry structure
*/
MEntry *me_get(FILE *fd){
	// pointer variable 
	MEntry *me = (MEntry * )malloc(sizeof(MEntry));
	me->surname = malloc(sizeof(char) * FULLNAMESIZE);
	me->zipcode = malloc(sizeof(char) * STRSIZE);
	me->full_address = malloc(sizeof(char) * (ZIPSIZE));

	// malloc returns void * pointer to n bytes of heap memory,
	// NULL if cannot
	// malloc failed
	if(me == NULL) {
	  free(me->surname);
	  free(me->zipcode);
	  free(me->full_address);
	  free(me);
	  return NULL;
	}
	if(me->surname == NULL) {
	  return NULL;
	}
	if(me->zipcode == NULL) {
	  return NULL;
	}
	if(me->full_address == NULL) {
	  return NULL;
	}
	

	// three input lines
	char fullname[FULLNAMESIZE];
	char streetaddress[STRSIZE];
	char cityzip[ZIPSIZE];


	// feof, non-zreo/true when end of file on stream
	// check if it is the end of file
	if(feof(fd)){
	  free(me->surname);
	  free(me->zipcode);
	  free(me->full_address);
	  free(me);
	  return NULL;
	}


	// fgets(s,n,fp) reads at most n-1 characters into s from fp,
	// terminates string with \0. returns NULL at end of file.
	fgets(fullname, FULLNAMESIZE, fd);
	fgets(streetaddress, STRSIZE, fd);
	fgets(cityzip, ZIPSIZE, fd);


	// strcpy(s,t) copy t to s, return s
	// strcat(s,t) append t to s, return s
	// put what have read so far into full_address
	strcpy(me->full_address, fullname);
	strcat(me->full_address, streetaddress);
	strcat(me->full_address, cityzip);


	int i, j;

	// get surname
	for(i = 0; fullname[i] != ','; i++){
	  me->surname[i] = (char)tolower(fullname[i]);
	}
	// end of surname string
	me->surname[i] = '\0';


	// atoi(s) returns integer value of s
	// get house_number
	me->house_number = atoi(streetaddress);
	


	// get zipcode
	for(i = 0, j = 0; ; i++){
	  if(cityzip[i] >= '0' && cityzip[i] <= '9'){
	    me->zipcode[j] = cityzip[i];
	    j++;
	  } else if (cityzip[i] == '\n') {
	    // end of zipcode string
	    me->zipcode[j] = '\0';
	    break;
	  }
	}

	return me;

}




 /* me_hash computes a hash of the MEntry, mod size 
    Computes a hash value for the surname+zipcode+house_number,
    Returning a value between 0 and size-1

    A hash table is a randomized data structure that supports the
    insert, delete, and find operations in expected O(1) time.
 */
unsigned long me_hash(MEntry *me, unsigned long size){
	unsigned long hashval = 0;
	int i;
	
	for(i = 0; me->surname[i] != '\0'; i++){
	  hashval += (int)me->surname[i];
	}
	for(i = 0; me->zipcode[i] != '\0'; i++){
	  hashval += (int)me->zipcode[i];
	}
	// house_number is an int
	hashval += me->house_number;
	hashval = hashval % size;
	return hashval;
}




/*me_print prints the full address on fd 
  fprintf print formatted output on fp
*/
void me_print(MEntry *me, FILE *fd){
	fprintf(fd, "%s", me->full_address);
}




/* me_compare compares two mail entries, returning <0, 0, >0 if
 * me1<me2, me1==me2, me1>me2

   Potential duplicates: identical surnames, zip codes, and house number

   strcmp returns <0, 0, >0
 */
int me_compare(MEntry *me1, MEntry *me2){
	int surnamecmp = 0, zipcodecmp = 0;
	
	surnamecmp = strcmp(me1->surname, me2->surname);
	zipcodecmp = strcmp(me1->zipcode, me2->zipcode);

	if(surnamecmp == 0){
	  if(zipcodecmp == 0){
	    if(me1->house_number == me2->house_number){
		return 0;
	    } // if 3
 	  } // if 2 
	} // if 1

	return -1;
}




/* me_destroy destroys the mail entry */
void me_destroy(MEntry *me){
	free(me->surname);
	free(me->zipcode);
	free(me->full_address); 
	free(me);
}


