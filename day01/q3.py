# Solution of question 3
# Check if a given string is a palindrome

input1 = input("Enter a string:")

def is_palindrome(text):
    text=text.lower()
    return text==text[::-1]

x = is_palindrome(input1)
print(x)
