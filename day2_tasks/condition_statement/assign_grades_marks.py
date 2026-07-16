#5. Write a program to assign grades based on marks (for example: A, B, C, Fail).
marks = int(input("Emter the Marks:"))

if marks >=85:
    print("A Grade")
elif marks >=65:
    print("B Grade")
elif marks >= 35:
    print("c Grade")
else:
    print("Fail")