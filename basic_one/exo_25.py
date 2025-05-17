# Python program that checks whether a specified value is contained within a group of values.
def is_present(value, data):
    return value in data  # Checks if value exists in the list

# Test cases
test_data = [1, 5, 8, 3]
print(f"3 -> {test_data} : {is_present(3, test_data)}")
print(f"-1 -> {test_data} : {is_present(-1, test_data)}")

