#Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
# Accept input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
