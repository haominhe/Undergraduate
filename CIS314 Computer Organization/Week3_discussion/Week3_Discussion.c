/* CIS 314    Week3 Lab_discussion
*
* Haomin He 
* 
* Write your own assembly program (.asm) format. The program should:
*/

//(i) Compute $t1 = ($t2 + $t3)*($t2 - $t3), where $t2 = 2, and $t3 =1 

#include <stdio.h>
#include <stdlib.h>

int main(){
    int t1;
    int t2 = 2;
    int t3 = 1;
    
    t1 = (t2 + t3) * (t2 - t3);
    
    printf("%d ",t1);


//(ii) Assign any int value to $t5 and Compute ($t1 = $t5*$t1) but via loop! 
//i.e. implement multiplication of 2 numbers in a loop 
//i.e. just break down the multiplication as loop of additions.

//<Hint: Start from .main, Functions used: add, addi, sub, mul; Use Labels for 
//loops as a go to statement with branching, which can be a regular branch/branch 
//on equal, branch on not equal, and so on>
     int t5 = 6; 
     int total = 0;
     int i;
     for (i = 0; i < t1; i++){
         total += t5; }
     t1 = total;
         
     printf("%d ",t1);
     
     return 0;


}







