/* program1.c 
 * 
 * CIS_314 Lab 3 
 * Fall 2015
 * Haomin He 
 * 
 * to emulate a Direct Mapped Cache
*/

/* 
* 1. Read 32 bit HEX address trace from the given file address.txt¡± <Input> 
*    
*/

#include <stdlib.h>
#include <stdio.h>

#define CacheSize 16
#define MAX_SIZE 500
#define FILE_NAME "address.txt" 

// simulate a direct mapped cache
// CacheSize 16
typedef struct{
              int valid;
              int tag;
              int data; // memory addresses 
              } cacheline;
              
   // declare the cache 
   cacheline cache[8];
     
   
void printCurrentCache(cacheline* cache);  // cacheline data type 
void printComputeValues(int hits, int misses, int total);

main() {
       FILE *in_file; // declare a pointer to a file
       unsigned int array[MAX_SIZE];
       int i = 0;
       int rv;
       int Numvalues;
       
       in_file = fopen ("address.txt", "r"); // read addresses from the input file
       if (in_file == NULL) perror ("Error opening file"); // print error

       else {
           while (i <= MAX_SIZE) {
                 rv = fscanf(in_file, "%x", &array[i]); // read as hex
                 if (rv != 1)
                    break;
                 i++;
                 } // while
           fclose(in_file);
           Numvalues = i;
           
           if (i > MAX_SIZE) {
                 printf("input too large \n");
              }
           else if (rv != EOF) {
                printf("error value \n");
                }
           else {
                //printf("end of the file \n");
                }
          
      printf("Read %d hex values: \n", Numvalues);
      //for (i = 0; i < Numvalues; i++){
          //printf("\t0X%08X \n", array[i]);
      //} // for
      
      } // else
      
      
     

/* 
* 2. Build a cache structure with required cache fields (index, tag, valid and data) and
*    following properties: 
*    a. Each cache line can fit 4 words.
*    b. Cache should have 8 entry lines.
*    c. Index and Tag must be stored in HEX form. Valid is 1 or 0. Data should be
*       the range of addresses whose value is stored in that cache block.
*       [Hint: Think about breaking down your address inputs into Tag + Index + Offset]
* 
*/
       
// address of the block = byte address / bytes per block 

// cache block id = (block address) mod (# of blocks in the cache) 
//                = (block address) mod 8 

// start simulating the cache

// initialize all valid bits of the cache to 0
   int a = 0;   
   for (a = 0; a < 8; a++){
       cache[a].valid = 0;
       cache[a].tag = 0;
       cache[a].data = 0;
   }// for 

    unsigned int current_address;
    unsigned int current_tag;
    unsigned int current_index;
    int hit_times = 0;
    int miss_times = 0;
    
    for (i = 0; i < Numvalues; i++){
              current_address = array[i];
              // remove the offset from the hex address
              current_address = current_address / 16; // shift right 4 positions, 2^4 = 16 bits
              
              // there are 3 bits in the index because we have have 8 entry lines
              // log(8) = 3, and 2^3 = 8
              current_tag = current_address / 8;
              current_index = current_address % 8; // use mod operation
              
              //printf("current_index: %x \ncurrent_tag: %x\n", current_index, current_tag);
              
              if (current_tag == cache[current_index].tag && cache[current_index].valid == 1 ) {
                  hit_times += 1;
                  //printf("Hit current_tag: %x \n", current_tag);
                  
                  } // if
              else {
                   miss_times += 1;
                   //printf("Miss current_tag: %x \n", current_tag);
                   cache[current_index].tag = current_tag;
                   cache[current_index].valid = 1;
                   cache[current_index].data = array[i] / 16 * 16;
                   } // else
          } // for
          
          printComputeValues(hit_times, miss_times, Numvalues);
          printCurrentCache(cache);        
 } //main       
       



/* 3. Write a function to print out the current state of your cache, i.e. at any given time,
*    if you call this function, it should print out the exact contents of the cache. 
*/
void printCurrentCache(cacheline* cache){
    printf("\n");
    printf("<Cache State>: \n");
    printf("Index      Tag               Valid         Data\n");
          
    int t = 0;
    for (t = 0; t < 8; t++) {
        printf("Index: %d   Tag: %X     Valid: %d      Data: MEM[%X] : MEM[%X]\n", t, cache[t].tag, cache[t].valid, cache[t].data, cache[t].data + 15);
          } // for 
} //printCurrentCache



/* 4. Write a function to print out the current value of number of hits, number of
*    misses, hit rate and miss rate. 
*/
void printComputeValues(int hits, int misses, int total) {
    printf("\n");
    printf("Number of hits: %d \n", hits);
    printf("Number of misses: %d \n", misses);
    printf("Hit Rate: %f \n", ((float)hits) / total);
    printf("Miss Rate: %f \n", ((float)misses) / total);
     
} // printComputeValue













































