# 2 - Write a function to check if a given string is a palindrome.

def is_palindrome(s):
    # Removing spaces and converting to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Taking input from the user
string = input("Enter a string: ")

# Checking if it's a palindrome
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
