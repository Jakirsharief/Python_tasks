#16. Write a function that returns the factorial of a number.
n = int(input())
def factor(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factor(n-1)
print(factor(n))