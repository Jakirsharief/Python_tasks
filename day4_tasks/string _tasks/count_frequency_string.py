#9. Write a program to count the frequency of each character in a string.
text = input("enter a string ")

for i in text:
    print(i,":",text.count(i))