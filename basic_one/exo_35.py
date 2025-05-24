#Python program that returns true if the two given integer values are equal or their sum or difference is 5.
def check_numbers(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

result = check_numbers(num1, num2)
print(result)
