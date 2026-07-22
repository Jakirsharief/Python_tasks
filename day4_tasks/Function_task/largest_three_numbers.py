#20. Write a Python program with a function that returns the largest of three numbers
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>= a:
        return b
    else:
        return c
print(largest(10,20,50))