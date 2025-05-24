# Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
def special_sum(a, b):
    total = a + b
    if 15 <= total <= 20:
        return 20
    return total
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
result = special_sum(num1, num2)
print("Result:", result)
