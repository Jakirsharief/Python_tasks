#4. Write a program to perform left shift (<<) and right shift (>>) operations on a number.

num = 10

L_shift = num << 2 # 1010 = (add two position left side ) = 101000 * 32 16 8 4 2 1 = 32+0+8+0+0+0 = 40
R_shift = num >> 2 # 1010 = (remove two right side position)= 10 =  0010 *  8 4 2 1 = 0+0+2 + 0 = 2 

print(" left shift", num ,"<<" , 2 ," :", L_shift)
print(" right shift", num ,"<<" , 2 ," :" ,R_shift)