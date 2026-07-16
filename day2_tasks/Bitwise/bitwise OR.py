#2. Write a program to perform bitwise OR (|) operation between two integers.

# a = 10  # 1010
# b = 5   # 0101


# or_sum = 10| 5 # 1 1 1 1 * 8 + 4 + 2 + 1

# print(a , "|" , b ,"= ", or_sum) #  15

num1 = int(input("Enter the 1St no:"))
num2 = int(input("Enter the 2nd no:"))

sum = num1| num2

print(num1 ,"|", num2,"=", sum)