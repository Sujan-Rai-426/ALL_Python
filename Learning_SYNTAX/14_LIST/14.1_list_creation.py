# Empty list
empty_list = []
empty_list = list()

# List with elements
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

# Using list() constructor
chars = list('hello')  # ['h', 'e', 'l', 'l', 'o']
numbers = list(range(5))  # [0, 1, 2, 3, 4]

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]