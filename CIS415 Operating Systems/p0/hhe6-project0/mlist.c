/* 
	Name: Haomin He
	DuckID: hhe6
	CIS415 Project0
	Fall 2016
	This file is provided by Prof Joe Sventek. 
	I made modifications based on the original file.
	
	Resources:
	C Pointer to Pointer
	 

*/




#include "mlist.h"
#include <stdlib.h>
#include <stdio.h>

// MList is to hide the representation of a mailing list
/* An MList is a set of MEntrys, it is like a mailing list contains entries
   of personal addresses, each address entry contains basic information
   about this person, like surname, house number, zipcode, and full address.
   So here, use MEntry to define MList structure.
*/
typedef struct mlistnode {
	struct mlistnode *next;
	MEntry *entry;
} MListNode;

struct mlist {
	struct mlistnode *first;
	struct mlistnode *last;
	unsigned long listsize;
};




/* ml_create - created a new mailing list
   This is the constructor for this ADT, called no arg,
   returns a pointer to an MList. 
   returns NULL if it is unsuccessful
 */
MList *ml_create(void) {
	MList *p;

	if ((p = (MList *)malloc(sizeof(MList))) != NULL) {
		p->first = NULL;
		p->last = NULL;
		p->listsize = 50;
	}
	return p;
}



/* ml_add - adds a new MEntry to the list;
 * returns 1 if successful, 0 if error (malloc)
 * if you request that a duplicate to an existing entry be added,
   ml_add ignores the request, yet still returns 1.
   returns 1 if it is a duplicate 
 */
int ml_add(MList **ml, MEntry *me) {
	MList *p;
	MListNode *q;

	p = *ml;
	if (ml_lookup(p, me) != NULL){
		p->listsize += 1;
		return 1;}
	if ((q = (MListNode *)malloc(sizeof(MListNode))) == NULL)
		return 0;
	q->entry = me;
	q->next = p->first;
	p->first = q;
	if (!(p->last))
		p->last = q;
	if(p->listsize == 20)
		p->listsize += 20;
	return 1;
}



/* ml_lookup - looks for MEntry in the list, returns matching entry or NULL
   it looks for an entry in the list that matches *me, if found, it is 
   returned as the function value, if not, NULL is returned. 
 */
MEntry *ml_lookup(MList *ml, MEntry *me) {
	MList *p;
	MListNode *q;

	p = ml;
	for (q = p->first; q != NULL; q = q->next)
		if (me_compare(me, q->entry) == 0)
			return q->entry;
	return NULL;
}



/* ml_destroy - destroy the mailing list 
   returns all heap-allocated storage associated with the entries in the list.
*/
void ml_destroy(MList *ml) {
	MListNode *q;

	q = ml->first;
	while (q != NULL) {
		MListNode *r = q->next;
		me_destroy(q->entry);
		free(q);
		q = r;
	}
	free(ml);
}
