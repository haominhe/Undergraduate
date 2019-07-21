/*
Name: Haomin He
DuckID: hhe6
CIS415 Project2
Fall 2016
This is my own work. 

Resources: 
Lecture slides
Start files from Prof Joe Sventek
CIS 415 lab code
Pthreads tutorial on Canvas
Enumerated Types
Stackoverflow - C errors, Threads, Locks
*/


/*
 * Define the interface to the DiskDriver module that mediates access to
 * a disk device
 */

#include "sectordescriptor.h"
#include "sectordescriptorcreator.h" 
#include "block.h"
#include "pid.h"
#include "freesectordescriptorstore.h"
#include "diskdevice.h"
#include "diskdevice_full.h"
#include "voucher.h"
#include "diskdriver.h"
#include "BoundedBuffer.h"
#include "freesectordescriptorstore_full.h"
#include "generic_queue.h"
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define BUFFER 100


/*
Creating my own type for voucher. 
*/
typedef enum {fail, working, done} thisvstatus;
typedef enum {read, write} thisvtype;

/* To ensure the voucher is threadsafe by using mutex and conditional
variable. Use SectorDescriptor pointers for reading and writing*/
struct voucher {
	pthread_mutex_t thismutex;
	pthread_cond_t conditionvar;
	SectorDescriptor *thissector;
	thisvstatus status;
	thisvtype type;
};

// threads and buffers
pthread_t readthread;
pthread_t writethread;
BoundedBuffer *readbuffer;
BoundedBuffer *writebuffer;

/*FreeSectorDescriptorStore to store no longer used SectorDescriptor
DiskDevice is for making calls on an instance*/
FreeSectorDescriptorStore *thisfreesectordescriptorstore = NULL;
DiskDevice *thisdiskdevice = NULL;



// thread reading
void* threadreadfun(){
	//while true
	while(1){
		//the buffer isn't empty and it had a voucher with SectorDescriptor
		//calling thread to block until there is an item in the BB
		Voucher *voucherpointer = (Voucher*)blockingReadBB(readbuffer);
		//aquire the lock
		pthread_mutex_lock(&(voucherpointer->thismutex));
		/*read_sector: 1 is successful, the sector read is contaned in the
		SectorDescriptor
		0 is unsuccessful.*/
		if(read_sector(thisdiskdevice, voucherpointer->thissector) == 1){
			voucherpointer->status = done;			
		} else {
			voucherpointer->status = fail;
		}
		// wake up other threads
		pthread_cond_signal(&(voucherpointer->conditionvar));
		//release the lock
		pthread_mutex_unlock(&(voucherpointer->thismutex));		
	}//while
}




// thread writing
void* threadwritefun(){
	// while true
	while(1){
		//the buffer isn't empty and it had a voucher with SectorDescriptor
		//calling thread to block until there is an item in the BB
		Voucher *voucherptr = (Voucher*)blockingReadBB(writebuffer);
		//aquire the lock
		pthread_mutex_lock(&(voucherptr->thismutex));
		/*write_sector: 1 is successful, write sector to disk
		0 is unsuccessful.*/
		if(write_sector(thisdiskdevice, voucherptr->thissector) == 1){
			voucherptr->status = done;			
		} else {
			voucherptr->status = fail;
		}
		// wake up other threads
		pthread_cond_signal(&(voucherptr->conditionvar));
		//release the lock
		pthread_mutex_unlock(&(voucherptr->thismutex));	
	}//while
}



/*
 * called before any other methods to allow you to initialize data
 * structures and to start any internal threads.
 *
 * Arguments:
 *   dd: the DiskDevice that you must drive
 *   mem_start, mem_length: some memory for SectorDescriptors
 *   fsds_ptr: you hand back a FreeSectorDescriptorStore constructed
 *             from the memory provided in the two previous arguments
 */
BoundedBuffer *voucherbuffer;
void init_disk_driver(DiskDevice *dd, void *mem_start, unsigned long mem_length,
		      FreeSectorDescriptorStore **fsds){
	// create FreeSectorDescriptorStore
	*fsds = create_fsds();
	create_free_sector_descriptors(*fsds, mem_start, mem_length);
	// assign the disk device
	thisdiskdevice = dd;
	// create buffers to hold items
	readbuffer = createBB(BUFFER);
	writebuffer = createBB(BUFFER);
	voucherbuffer = createBB(BUFFER);
	//create read write threads
	pthread_create(&readthread, NULL, &threadreadfun, NULL);
	pthread_create(&writethread, NULL, &threadwritefun, NULL);
}




/*
 * the following calls are used to write a sector to the disk
 * the nonblocking call must return promptly, returning 1 if successful at
 * queueing up the write, 0 if not (in case internal buffers are full)
 * the blocking call will usually return promptly, but there may be
 * a delay while it waits for space in your buffers.
 * neither call should delay until the sector is actually written to the disk
 * for a successful nonblocking call and for the blocking call, a voucher is
 * returned that is required to determine the success/failure of the write
 */
void blocking_write_sector(SectorDescriptor *sd, Voucher **v){
	/*read the voucher buffer and initialize the voucher
	block calling thread until there is an item in the BB*/
	*v = (Voucher*) blockingReadBB(voucherbuffer);
	(*v)->thissector = sd;
	(*v)->status = working;
	(*v)->type = write;
	/* write methods on BB, blocking call causes calling thread to 
	block until there is room in the BB*/
	blockingWriteBB(writebuffer, *v);
}



int nonblocking_write_sector(SectorDescriptor *sd, Voucher **v){
	/*read the voucher buffer first and initialize the voucher
	nonblockingread returns 1 if item was successfully retrived from 
	the BB, 0 otherwise	*/
	int resultholder;
	resultholder = nonblockingReadBB(voucherbuffer, (void**)v);
	// read not succeed 
	if(resultholder == 0){return 0;}
	else{
		(*v)->thissector = sd;
		(*v)->status = working;
		(*v)->type = write;
	}
	//nonblockingWriteBB: 1 if item successfully store in the BB
	// 0 otherwise
	int bufferreturnstate;
	bufferreturnstate = nonblockingWriteBB(writebuffer, *v);
	return bufferreturnstate;
}




/*
 * the following calls are used to initiate the read of a sector from the disk
 * the nonblocking call must return promptly, returning 1 if successful at
 * queueing up the read, 0 if not (in case internal buffers are full)
 * the blocking call will usually return promptly, but there may be
 * a delay while it waits for space in your buffers.
 * neither call should delay until the sector is actually read from the disk
 * for successful nonblocking call and for the blocking call, a voucher is
 * returned that is required to collect the sector after the read completes.
 */
void blocking_read_sector(SectorDescriptor *sd, Voucher **v){
	/*read the voucher buffer and initialize the voucher
	block calling thread until there is an item in the BB*/
	*v = (Voucher*)blockingReadBB(voucherbuffer);
	(*v)->thissector = sd;
	(*v)->status = working;
	(*v)->type = read;
	/* write methods on BB, blocking call causes calling thread to 
	block until there is room in the BB*/
	blockingWriteBB(readbuffer, *v);
}



int nonblocking_read_sector(SectorDescriptor *sd, Voucher **v){
	/*read the voucher buffer first and initialize the voucher
	nonblockingread returns 1 if item was successfully retrived from 
	the BB, 0 otherwise	*/
	int resultholder;
	resultholder = nonblockingReadBB(voucherbuffer, (void**)v);
	// read not succeed 
	if(resultholder == 0){return 0;}
	else{
		(*v)->thissector = sd;
		(*v)->status = working;
		(*v)->type = read;
	}
	//nonblockingWriteBB: 1 if item successfully store in the BB,
	// 0 otherwise
	int bufferreturnstate;
	bufferreturnstate = nonblockingWriteBB(readbuffer, *v);
	return bufferreturnstate;
}



/*
 * the following call is used to retrieve the status of the read or write
 * the return value is 1 if successful, 0 if not
 * the calling application is blocked until the read/write has completed
 * if a successful read, the associated SectorDescriptor is returned in *sd
 */
int redeem_voucher(Voucher *v, SectorDescriptor **sd){
	int currentstatus;
	//acquire the lock
	pthread_mutex_lock(&(v->thismutex));

	/*the associated SectorDescriptor has not been read or written yet,
	it has to wait untill condition variable gets signalled by a 
	read or write signal */
	while(v->status == working){
		pthread_cond_wait(&(v->conditionvar), &(v->thismutex));
	} //while
	/*At this point, we know that the SectorDescriptor has either been 
	successful or failed
	blockingWriteBB: block calling thread until there is an item in the BB*/
	blockingWriteBB(voucherbuffer, v);

	/*if the type is read, we get the SectorDescriptor value.
	if the type is write, we return the SectorDescriptor to store 
	*/
	if(v->type == read) {*sd = v->thissector;}
	else{blocking_put_sd(thisfreesectordescriptorstore, v->thissector);}

	/*see whether status is fail, working or done*/
	currentstatus = v->status;
	pthread_mutex_unlock(&(v->thismutex));
	pthread_cond_destroy(&(v->conditionvar));
	pthread_mutex_destroy(&(v->thismutex));

	return (currentstatus == done);
}
