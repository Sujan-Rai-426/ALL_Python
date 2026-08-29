# NOTE: pop() - Remove and return element


# Syntax: list.pop(index) - removes element at index
fruits = ['apple', 'banana', 'orange', 'mango']

# Remove last element (default)
last = fruits.pop()
print(last)  # 'mango'
print(fruits)  # ['apple', 'banana', 'orange']

# Remove at specific index
removed = fruits.pop(1)
print(removed)  # 'banana'
print(fruits)  # ['apple', 'orange']

# Pop from empty list raises IndexError
try:
    empty = []
    empty.pop()
except IndexError as e:
    print(f"Error: {e}")