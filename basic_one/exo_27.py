 # Python program that concatenates all elements in a list into a string and returns it.
def concat_list(lst): return ''.join(map(str, lst))

print(concat_list([1, "hello", 3.5, "world"]))  # Output: "1hello3.5world"
