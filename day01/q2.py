# Solution of question 2
#Create a Python program to count the number of vowels in a given string.

vowels = ["a","e","i","o","u"]
count =0
text = "Abhishek is a good boy".lower()

for index,char in enumerate(text):
    if char in vowels:
        count+=1
        print(f"Vowel '{char}' and its position '{index}'")

print(f"Total number of vowels: {count}")
