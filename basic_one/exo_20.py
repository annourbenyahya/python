#Python program that returns a string that is n (non-negative integer) copies of a given string.
def repeat_string(s, n):
    return s * n  # Multiply string by n to repeat it

# Get user input
text = input("Enter a string: ")
num = int(input("Enter a non-negative integer: "))

# Print result
print("Result:", repeat_string(text, num))
