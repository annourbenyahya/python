#Python program that computes the greatest common divisor (GCD) of two positive integers.
import math

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

gcd = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")
