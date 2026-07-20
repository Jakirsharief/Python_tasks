#7. Write a program to check whether a key exists in a dictionary.
dictionary = {1:"ashok",2:"jhons",3:"abhiram",4:"ram"}

key = int(input("enter the key"))
if key in dictionary:
    print("key exist")
else:
    print("key not exists")