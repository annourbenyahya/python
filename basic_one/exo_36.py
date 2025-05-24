#Python program to add two objects if both objects are integers.
def add_if_integers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Both objects must be integers."
print(add_if_integers(5, 3))        
print(add_if_integers(5, "3"))      
print(add_if_integers(2.5, 7))      
print(add_if_integers(10, -4))      
