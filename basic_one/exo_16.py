 #Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

def difference(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return abs(n - 17)

# Get user input
num = float(input("Enter a number: "))
print("Result:", difference(num))

