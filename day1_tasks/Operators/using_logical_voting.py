#4. Write a program using logical operators to check age eligibility for voting. 
eligibiltiy = int(input("Enter the Age:"))
print(eligibiltiy >= 18 and eligibiltiy <=100) #18 to high and 100 to low for eligibiltiy.
if eligibiltiy >= 18:
    print("eligibility for voting.")
elif eligibiltiy< 18:
    print("not eligibility for voting.")
    