/* Winter2016 CIS330 Assignment3 Haomin He */
/* Problem 3*/
/* directory.c: implement a phone directory application */

/* Implement a simple people directory data structure.
- Design a dynamic data structure that can store people's names and phone numbers
- Implement functions to add and delete individual person's information. You can 
  also add more functions. Put these functions in directory.c (also create 
  directory.h with the function prototypes).
- Be sure to handle invalid user inputs without crashing. 
*/


#include <stdio.h>
#include "directory.h"
#include <stdlib.h>
#include <string.h>


// from the example session, we need to get input name and phone number from the 
// user.
// pass pointer parameter to this function
void storePeopleNameAndPhNum(thisPerson *thisPerInfo, char *thisName, char *thisNum) {
     // get a pointer to point to the info address
     thisPerson *tempInfo = thisPerInfo;
     
     // -> access elements of a struct/class that is a pointer instead of a reference
     // as long as the Info list has a next person, loop through the list, until 
     // got to the last person. The other case is that the list is empty.
     while(tempInfo->nextPerson != NULL) {
         tempInfo = tempInfo->nextPerson;
         } // while
         
     // locate the memory
     tempInfo->personPtr = (onePerson *) malloc (sizeof(onePerson));
     tempInfo->personPtr->personName = (char *) malloc (strlen(thisName) * sizeof(char));
     tempInfo->personPtr->personNum = (char *) malloc (strlen(thisNum) * sizeof (char)); 
     
     // copy input name and number to the structure variable
     strcpy(tempInfo->personPtr->personName, thisName);
     strcpy(tempInfo->personPtr->personNum, thisNum);
     
     // set up the next person info, get the memory space
     tempInfo->nextPerson = (thisPerson *) malloc (sizeof(thisPerson));
     // the next person's value is NULL at the beginning, and next's next person
     // is NULL as well
     tempInfo->nextPerson->personPtr = NULL; 
     tempInfo->nextPerson->nextPerson= NULL;
     
     } // storePeopleNameAndPhNum


// ** is a pointer to a pointer
// delete individual person's information
int deleteInfo(thisPerson **thisPerInfo, int aNumber){
    thisPerson *tempInfo = *thisPerInfo;
    
    // set up previous person pointer, so that we can delete and without
    // losing contact info
    thisPerson *previousPerson = NULL;
    // keep track of looping index 
    int counter = 0;
    counter += 1; // starts at 1
    
    if(tempInfo->personPtr == NULL){
        return 0; // check case: if nothing in the list, or end of the list
        } // if
        
    // loop through the list, also keep counting     
    // when the list is not empty, loop until counter hits aNumber
    while(tempInfo->nextPerson != NULL && counter < aNumber){
        counter += 1; // increment the counter first
        // move to the next person node
        previousPerson = tempInfo;
        tempInfo = tempInfo->nextPerson;                      
        } // while
    
    // end of the list case
    if(tempInfo->nextPerson == NULL) {
        return 0;
        } // if
        
    // in the middle of list case
    // set the next person value
    if (previousPerson != NULL) {
        // because we delete the current person node, so the previous's next person
        // pointer points to current person's next 
        previousPerson->nextPerson = tempInfo->nextPerson;
        } // if
    else { // previous person == NULL, at the beginning of the list
           // set value of next person
           // because we delete the current first person node, so the second person
           // node becomes the head of the list
         *thisPerInfo = tempInfo->nextPerson;
         } // else
    
    // free all the memory spaces
    // if current person node is not NULL
    if(tempInfo != NULL) {
      // set current person node's next to NULL
      tempInfo->nextPerson = NULL;
      // if current person node has a value
      if(tempInfo->personPtr != NULL) {
         // free all the contact info
         free(tempInfo->personPtr->personName);
         free(tempInfo->personPtr->personNum);
         // free the current person pointer, and set it to NULL
         free(tempInfo->personPtr);
         tempInfo->personPtr = NULL;         
         } // inner if
      // free the list
      free(tempInfo);
      } // outer if 
      
    return 1;
    } // deleteInfo
     

void printAllInfo(thisPerson *thisPerInfoPrint){
     thisPerson *tempInfo = thisPerInfoPrint;
     printf("Current directory: \n");
     
     // loop through the list
     int counter = 0;
     counter += 1; // starts at 1
     // while not hit the end of the list
     while(tempInfo->nextPerson != NULL) {
         // current person node has a value
         if (tempInfo->personPtr != NULL) {
             // print all info of the person
             printf("%d. %s, %s\n", counter, tempInfo->personPtr->personName, tempInfo->personPtr->personNum);
             counter++;
               } // if 
         // increment to next person, continue looping
         tempInfo = tempInfo->nextPerson;                           
         } // while   
     } // printAllInfo






















