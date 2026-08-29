# Syntax: del list[index]
fruits = ['apple', 'banana', 'orange', 'mango', 'grape']

# Delete single element
del fruits[1]  # ['apple', 'orange', 'mango', 'grape']

# Delete slice
del fruits[1:3]  # ['apple', 'grape']

# Delete entire list
del fruits

# Delete by index with negative
numbers = [1, 2, 3, 4, 5]
del numbers[-1]  # [1, 2, 3, 4]
del numbers[-2:]  # [1, 2]