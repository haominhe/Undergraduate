#----------------------------------------------------------#
# Program 2: Recursive Binary Search in MIPS
# a mips program that performs the binary search recursively
#
# CIS 314 lab 2 assignment 
# Haomin He
#----------------------------------------------------------#

####################### Text Section #######################
# The function will take the following 4 inputs:
# $a0 base address of the array
# $a1 target
# $a2 starting index
# $a3 ending index
# It will return the index of the target (or -1 if not found) in $v0. 

.text
.globl main

main: 
    la      $a0, my_array       # put pointer to my_array in $a0
    
    lw      $a1, key_search     # load the value search for
    lw      $a2, start_index    # load startind_index
    lw      $a3, end_index      # load the ending_index
    lw      $t5, array_size     # load base address of array_size = 11
                                # into a4
    lw      $t6, middle         # load middle_index

    
    add     $a2, $0, $0         # the start_index = 0
    add     $a3, $t5, $zero     # the end_index = array_size - 1
    addi    $a3, $a3, -1
    

    


    #addi    $a1, $zero, 7       # a1 = 7 load immediate
    #jal     binary_search       # binary_search(7)
    #add     $s2, $v0, $zero     # $s2 = binary_search(7) = 3


    li     $a1, 21             # a1 = 21 load immediate
    jal     binary_search      # binary_search(21)
    add     $s3, $v0, $zero    # $s3 = binary_search(21) = 9


exit:
    li      $v0, 10
    syscall




############################################################
# recursive binary search function

binary_search:                     # prologue  
        addi    $sp, $sp, -20      # move stack pointer
        sw      $s4, 0($sp)
        sw      $s5, 4($sp)
        sw      $s6, 8($sp)
        sw      $s7, 12($sp)
        sw      $ra, 16($sp)


        add     $t6, $a3, $a2      # let middle = end + start
        sra     $t6, $t6, 1        # shift right arithmetic, compute
                                   # middle = (start + end) / 2
        sll     $t0, $t6, 2        # shift left logical, multiply middle 
                                   # by 4, and store the number in t0
        add     $t7, $t0, $a0      # from my_array a0, find my_array[middle]
        lw      $t1, 0($t7)        # load value of my_array[middle]


        beq     $t1, $a1, foundval # if my_array[middle] == key_search
                                   # branch to function foundval


        slt     $t3, $a3, $a2       # if end_index < start_index, where t3 = 1
                                    # not found the key_search
        beq     $t3, 1, notfound





        slt     $t2, $t1, $a1      # set on less than (signed)
                                   # compare my_array[middle] to key_search
                                   # t2 becomes 1 if my_array[middle] < key_search

        beq     $t2, $0, left_part # branch on equal, if t2 = 0, means
                                   # my_array[middle] >= key_search
                                   # in the left part of array, search for the key_search

        beq     $t2, 1, right_part # branch on equal, if t2 = 1, means
                                   # my_array[middle] < key_search
                                   # in the right part of array, search for the key_search

                                
        
        
        


foundval:
        add    $v0, $t6, $zero     # return the value
        
        j       return

        


left_part: 
        addi     $a3, $t6, -1      # if my_array[middle] >= key_search
                                   # end_index = middle - 1
        jal     binary_search      # go back and search again


right_part:
                                   # if my_array[middle] < key_search
        addi    $a2, $t6, 1        # start_index = middle + 1
        jal     binary_search      # run binary_search again
        



return:
        lw      $s4, 0($sp)        # epilogue
        lw      $s5, 4($sp)        # pop stack
        lw      $s6, 8($sp)
        lw      $s7, 12($sp)
        lw      $ra, 16($sp)
        addi    $sp, $sp, 20       # move stack pointer
        jr      $ra                # return     


notfound:
        li      $v0, -1            # if not find key_search in my_array
                                   # return -1
        j       return

                                   




####################### Data Section #######################
            .data
my_array:   .word 1,4,5,7,9,12,15,17,20,21,30    # an int array
array_size:     .word 11                         # the array size
start_index:    .word 0                          # starting_index
end_index:      .word 1                          # ending_index
middle:         .word 1                          # middle_index
key_search:     .word 1                          # the value to search for


































