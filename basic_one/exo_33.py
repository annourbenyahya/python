#Python program to sum three given integers. However, if two values are equal, the sum will be zero.
def custom_sum(a, b, c):
    return 0 if a == b or a == c or b == c else a + b + c

# Example usage
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

print(f"The result is: {custom_sum(num1, num2, num3)}")



