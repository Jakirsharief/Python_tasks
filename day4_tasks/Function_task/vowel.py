#19. Write a function that takes a string as input and returns the number of vowels
text = input()
def count_vowels(text):
    vowels= "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count +=1
    return count
print(count_vowels(text))
