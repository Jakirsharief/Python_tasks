#15. Write a function to check whether a number is even or odd.
# num = int(input())
# if num % 2 ==0:
#     print("even")
# else:
#     print("odd")
n = int(input())
def check_wheater(n):
    if n % 2 ==0:
        return("even")
    else:
        return("odd")
print(check_wheater(n))