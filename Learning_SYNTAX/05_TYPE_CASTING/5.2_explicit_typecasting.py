# NOTE: Explicit Type Conversion (Type Casting): Done manually by the programmer using built-in functions.

# Float to Int
pi = 3.14159
print(int(pi))   # Output: 3

# String to Int
num_str = "100"
print(int(num_str) + 50)  # Output: 150

# Boolean to Int
print(int(True))   # Output: 1
print(int(False))  # Output: 0

# Int to Float
x = 5
print(float(x))  # Output: 5.0

# String to Float
price = "49.99"
print(float(price))  # Output: 49.99

# Int/Float to String
age = 25
message = "I am " + str(age) + " years old."
print(message)  # Output: I am 25 years old.

# Tuple to List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)        # Output: [1, 2, 3]

# List to Set (removes duplicates)
my_list = [1, 2, 2, 3, 3]
my_set = set(my_list)
print(my_set)         # Output: {1, 2, 3}

# String to List (splits into individual characters)
word = "Python"
print(list(word))     # Output: ['P', 'y', 't', 'h', 'o', 'n']

pairs = [("name", "Alice"), ("age", 30)]
my_dict = dict(pairs)
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}