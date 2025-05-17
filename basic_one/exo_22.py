# Python program to count the number 4 in a given list.
def count_fours(lst):
    return lst.count(4)

# Example usage
numbers = [1, 4, 2, 4, 3, 4, 5]
print(f"Number of times 4 appears: {count_fours(numbers)}")
