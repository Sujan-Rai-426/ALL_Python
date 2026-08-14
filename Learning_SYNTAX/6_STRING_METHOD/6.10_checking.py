# NOTE:These methods check the contents of a string and return True or False.

# NOTE: startswith() and endswith(): Checks if a string starts or ends with a specific substring.
filename = "report.pdf"
print(filename.startswith("rep"))  # Output: True
print(filename.endswith(".pdf"))   # Output: True



# NOTE: isalnum(): Checks if all characters are alphanumeric (letters and numbers only, no spaces or symbols).
print("Python3".isalnum())   # Output: True
print("Python 3!".isalnum()) # Output: False (due to space and exclamation)



# NOTE: isalpha(): Checks if all characters are alphabetic letters.
print("Hello".isalpha())     # Output: True
print("Hello123".isalpha())  # Output: False



# NOTE: isdigit(): Checks if all characters are digits.
print("12345".isdigit())     # Output: True
print("123.45".isdigit())    # Output: False (decimal point is not a digit)



# NOTE: isspace(): Checks if all characters are whitespaces.
print("   ".isspace())       # Output: True



# NOTE: islower() and isupper(): Checks casing.
print("hello".islower())     # Output: True
print("HELLO".isupper())     # Output: True