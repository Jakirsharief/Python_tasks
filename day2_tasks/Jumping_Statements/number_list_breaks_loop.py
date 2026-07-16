#4. Write a program that searches for a number in a list and breaks the loop when found.
numbers = (10,20,30,40,50)
sreach = int(input("sreaching the number"))
for number in numbers:
    if number == sreach:
        print("found in the list")
        break
else:
        print("not found")


