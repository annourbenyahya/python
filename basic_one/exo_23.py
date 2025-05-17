# Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
def get_copies(s, n):
    return s * n if len(s) < 2 else s[:2] * n  # Use first 2 chars if length >= 2

# Get user input
text = input("Enter a string: ")
num = int(input("Enter a non-negative integer: "))

# Print result
print("Result:", get_copies(text, num))
