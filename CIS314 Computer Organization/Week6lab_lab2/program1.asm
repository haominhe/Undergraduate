#----------------------------------------------------------#
# Program 1: Iterative Binary Search in MIPS
# a mips program that performs the binary search iteratively
#
# CIS 314 lab 2 assignment 
# Haomin He
#----------------------------------------------------------#

####################### Text Section #######################
# <1> the base address of the array from $s0,
# <2> size of the array from $s1 and
# <3> the element you¡¯re searching for in the array from $s2.
# It will return the index of the element searched for in $v0.

.text
.globl main

main: 
        la  $s0, my_array    # put pointer to my_array in $s0
        lw  $s1, array_size  # put array_size (not pointer) in $s1
                             # Load the base address of array into 
                             # $s0 using¡®la¡¯ and load the size of 
                             # array into $s1 using ¡®lw¡¯
        lw  $s2, key_search  # the value to search for


        addi    $s2, $zero, 15
        jal     binary_search   # binary_search(15)
        add     $s3, $v0, $zero # $s3 = binary_search(15) = 6

        addi    $s2, $zero, 4
        jal     binary_search   # binary_search(4)
        add     $s4, $v0, $zero # $s4 = binary_search(4) = 1

        addi    $s2, $zero, 30
        jal     binary_search   # binary_search(30)
        add     $s5, $v0, $zero # $s5 = binary_search(30) = 10

        addi    $s2, $zero, 0
        jal     binary_search   # binary_search(15)
        add     $s6, $v0, $zero # $s6 = binary_search(15) = -1

exit:
        li      $v0, 10
        syscall

        



############################################################
# iterative binary search function

binary_search:                  # prologue
        addi $sp, $sp, -20      # move stack pointer
        sw   $s3, 0($sp)
        sw   $s4, 4($sp)
        sw   $s5, 8($sp)
        sw   $s6, 12($sp)
        sw   $ra, 16($sp)
        

                                # body od the function
        li  $t0, 0              # bottom = 0
        add $t1, $s1, -1        # top = array_list - 1

while:  bgt $t0, $t1, srchnone  # branch on greater than
                                # if bottom > top, not found the value
        add $t2, $t0, $t1       # middle = t2
        srl $t2, $t2, 1         # middle = (bottom + top) / 2
                                # shift right logical by a constant number of bits
        sll $t3, $t2, 2         # shift left logical by a constant number of bits
                                # byte offset of my_array[middle] into list
        add $t3, $t3, $s0       # address of my_array[middle]
        lw  $t4, 0($t3)         # t4 = my_array[middle]

        bne $s2, $t4, not_equal # branch on not equal
                                # if key_search != my_array[middle]
                                # branch to the function 
                                
        move $v0, $t2           # if key_search == my_array[middle]
        jr   $ra                # return t2 = mid
                                # move integer to: $v0 = $t2
                                # jump to return address in $ra


not_equal: 
        bgt  $s2, $t4, greater  # if key_search > my_array[middle]
                                # branch to the function
        addi $t1, $t2, -1       # if key_search < my_array[middle]
                                # top = middle - 1
        j    while              # unconditonal jump to program label target


greater:
        addi $t0, $t2, 1        # if key_search > my_array[middle]
                                # bottom = middle + 1
        j    while

srchnone:
        li  $v0, -1             # if key_search is not found, return -1
        jr  $ra                 # move integer to: $v0 = -1
                                # jump to return address in $ra
        
    
# return
        lw   $s3, 0($sp)        # epilogue
        lw   $s4, 4($sp)        # pop stack
        lw   $s5, 8($sp)
        lw   $s6, 12($sp)
        lw   $ra, 16($sp)
        addi $sp, $sp, 20       # move stack pointer
        jr   $ra                # return           







####################### Data Section #######################
            .data
my_array:   .word 1,4,5,7,9,12,15,17,20,21,30    # an int array
array_size: .word 11                             # the array size
key_search: .word 0                              # the value to search for



























