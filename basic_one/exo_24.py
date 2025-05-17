#Python program to test whether a passed letter is a vowel or not.
def is_vowel(c): return c.lower() in "aeiou"

char = input("Enter a letter: ")
print("Vowel" if len(char) == 1 and char.isalpha() and is_vowel(char) else "Not a vowel")
