# CIS 314 Week3 Lab_discussion
# Haomin He 
# Write your own assembly program (.asm) format. 

.data

.text
.globl main

main:
    li $t2, 2
    li $t3, 1
    add $t2, $t2, $t3
    sub $t3, $t2, $t3
    add $t1, $t2, $t3
    syscall


    li $t5, 6
    li $a0, 0
    ori $t0, $t1, 0
    add $a0, $a0, $t5
    addi $t0, $t0, -1
    bgtz $t0, loop 
