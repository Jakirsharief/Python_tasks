#4. Write a program to check whether an element exists in a tuple.
numbers = (5,10,15,20,25)
search = int(input("Enter The Number:"))

if search in numbers:
    print("Element exists")
else:
    print("Element does not exists")