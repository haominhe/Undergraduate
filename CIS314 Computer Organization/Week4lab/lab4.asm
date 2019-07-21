# Haomin He
# CIS 314 Lab4

.data
    arraysize: .word 6
    array: .word 6,3,2,6,3,1
    sum: .word 0

.text
.globl main

main:
    lw $s0, array
    lw $s1, arraysize

    li $t0, 0
    li $t1, $s0
    lw $s2, sum

loop:
    beq $t0, $s1, end
    lw $t1, 
    add $s2, $s2, 
    addi $t0, $t0, 1

j   loop

end:
    













    




    move $a0 $s2
    li $v0 1
    syscall