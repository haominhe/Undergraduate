/* cache_arrays.c 
 * CIS_314 in lab activity
 * Nov 16 2015
*/


#include <stdio.h>  //printf, fscanf
#include <stdlib.h> //exit
#include <time.h>   //clock

#define N     2000
#define TRUE  1
#define FALSE 0

int** make_array();
void fill_arrays(int** array_1, int** array_2, int** array_3);
void run_tests(int** array_1, int** array_2, int** array_3);
void do_bad_addition(int** array_1, int** array_2, int** array_3);
void do_good_addition(int** array_1, int** array_2, int** array_3);
int  check_arrays(int** array_1, int** array_2, int** array_3);
void print_arrays(int** array_1, int** array_2, int** array_3);
void free_arrays(int** array_1, int** array_2, int** array_3);

int main(void) {
   int **array_1;
   int **array_2;
  int **array_3;
   //make_arrays(array_1, array_2);
   array_1 = make_array();
   array_2 = make_array();
   array_3 = make_array();
   if(check_arrays(array_1, array_2,array_3)) {
      fill_arrays(array_1, array_2, array_3);
      print_arrays(array_1, array_2,array_3);
      run_tests(array_1, array_2,array_3);
      free_arrays(array_1, array_2,array_3);
   } else {
   	  printf("ERROR: Array check failed.\n");
   }

   return 0;
}


int** make_array() {
   int i = 0;
   int** array_1;
   printf("making array...");
   array_1 = (int**) malloc(N * sizeof(int*));
      if( (array_1 != NULL) ) {
      for(i = 0; i < N; i++) {
         array_1[i] = (int*) malloc(N * sizeof(int));
      }
      printf("done\n");
   } else {
      printf("error\n");
   }
   return array_1;
}

void fill_arrays(int** array_1, int** array_2, int** array_3) {
   int i = 0, j = 0;

   for(i = 0; i < N; i++) {
      for(j = 0; j < N; j++) {
         array_1[i][j] = 2;
         array_2[i][j] = 2;
      }
   }
   
}

int check_arrays(int** array_1, int** array_2, int** array_3) {
   int ok = TRUE, i = 0;

   printf("checking base arrays...");
   if(array_1 == NULL) ok = FALSE;
   if(array_2 == NULL) ok = FALSE;
   printf("done\n");
   if(ok) {
      printf("checking individual arrays...");
      for(i = 0; i < N; i++) {
         if(array_1[i] == NULL) 
            ok = FALSE;
         if(array_2[i] == NULL) 
            ok = FALSE;
         if(ok == FALSE) {
         	printf("\n\n%d\n\n", i);
         	break;
         }
      }
      printf("done\n");
   }
   return ok;
}


void run_tests(int** array_1, int** array_2, int** array_3) {
   clock_t t1, t2;

   t1 = clock();
   do_bad_addition(array_1, array_2, array_3);
   t2 = clock();
   print_arrays(array_1, array_2, array_3);
   printf("\nbad addition takes %.2f ms\n\n", (float)(t2 -t1)/CLOCKS_PER_SEC );
   
   t1 = clock();
   do_good_addition(array_1, array_2, array_3);
   t2 = clock();
   print_arrays(array_1, array_2, array_3);
   printf("\ngood addition takes %.2f ms\n\n", (float)(t2 -t1)/CLOCKS_PER_SEC );
   
}


void do_bad_addition(int** array_1, int** array_2, int** array_3) {
     int i = 0, j = 0; 
     
     for(j = 0; j < N; j++) {
      for(i = 0; i < N; i++) { 
            array_3[i][j] = array_1[i][j] + array_2[i][j];
            }
            }

}

void do_good_addition(int** array_1, int** array_2, int** array_3){
     int i = 0, j = 0; 
     
     for(i = 0; i < N; i++) {
      for(j = 0; j < N; j++) { 
            array_3[i][j] = array_1[i][j] + array_2[i][j];
            }
            }

}

void print_arrays(int** array_1, int** array_2, int **array_3) {
   int i = 0, j = 0;

   int max = N;
   if(max > 25) max = 15;

   printf("\n\nArray 1:\n");
   for(i = 0; i < max; i++) {
      for(j = 0; j < max; j++) {
         printf("%5d", array_1[i][j]);
      }
      printf("\n");
   }

   printf("\n\nArray 2:\n");
   for(i = 0; i < max; i++) {
      for(j = 0; j < max; j++) {
         printf("%5d", array_2[i][j]);
      }
      printf("\n");
   }
  
  printf("\n\nArray 3:\n");
  for(i = 0; i < max; i++) {
    for(j = 0; j < max; j++) {
      printf("%5d", array_3[i][j]);
    }
    printf("\n");
  }
}

void free_arrays(int** array_1, int** array_2, int ** array_3) {
   int i = 0, j = 0;

   for(i = 0; i < N; i++) {
      free(array_1[i]);
      free(array_2[i]);
      free(array_3[i]);

   }

   free(array_1);
   free(array_2);
   free(array_3);
}
