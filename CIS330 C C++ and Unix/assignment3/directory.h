/* Winter2016 CIS330 Assignment3 Haomin He */
/* Problem 3*/
/* directory.h: a header file */

////////////////////////////////////
#ifndef DIRECTORY_H_
#define DIRECTORY_H_

/* create user defined data types
   structure: group of related data / collection of fields 
 */
struct allPeople {
       // create pointers
       char *personName;
       char *personNum;        
       }; // struct
typedef struct allPeople onePerson;

typedef struct thisPerson thisPerson;
struct thisPerson{
       // create current person pointer
       onePerson *personPtr;
       // keep track of the next person in the list
       thisPerson *nextPerson;
       }; // struct
        

void storePeopleNameAndPhNum(thisPerson *thisPerInfo, char *thisName, char *thisNum);
int deleteInfo(thisPerson **thisPerInfo, int aNumber);
void printAllInfo(thisPerson *thisPerInfoPrint);
#endif /* DIRECTORY_H_ */





