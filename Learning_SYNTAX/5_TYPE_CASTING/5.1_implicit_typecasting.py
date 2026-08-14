# NOTE: Implicit Type Conversion: Python automatically converts a smaller data type to a wider data type to prevent data loss. For example, adding an integer and a float results in a float.

x = 10     # int
y = 2.5    # float

result = x + y
print(result)         # Output: 12.5
print(type(result))   # Output: <class 'float'>