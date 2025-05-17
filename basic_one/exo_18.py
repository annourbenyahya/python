#Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def custom_sum(a, b, c):
    total = a + b + c
    return total * 3 if a == b == c else total

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Print result
print("Result:", custom_sum(num1, num2, num3))

