#3. Write a program to find the sum of numbers from 1 to N using a loop.
n = int(input("Enter the number"))
sum = 0
for i in range(1, n + 1): # i = 1, i = 2,
    sum = sum + i # 0 +1 = 1 , 1 +2 = 3 , 3+3 = 6 , 6 + 4 = 10 , 10+5 =15

    print(sum)