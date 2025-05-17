#Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
def add_prefix(s):
    return s if s.startswith("Is") else "Is" + s

# Get user input
string = input("Enter a string: ")
print("Result:", add_prefix(string))
