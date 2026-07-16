#8. Write a program to find the second largest number in a list.
x = [7,8,9,74,78,4,2]

x.sort()
second_largest = x[-2]

print(x)
print("second_largest :",second_largest)