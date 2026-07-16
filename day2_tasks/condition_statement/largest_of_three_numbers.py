#3. Write a program to find the largest of three numbers using if-elif-else.
num1 = int(input("Enter the 1st Number:")) #10
num2 = int(input("Enter the 2nd Number:")) #20
num3 = int(input("Enter the 3rd Number:")) #30

if num1 >= num2 and num1>=num3:  #30>20 and 30>10 T 
    print("largest number :",num1) 
elif num2 >= num1 and num2 >= num3: # 20>10 and 20>30 f 
    print("largest number :", num2)
else:                                # 10 f
    print("largest number :", num3)
