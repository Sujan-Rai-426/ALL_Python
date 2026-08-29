
# NOTE: 1. remove() - Remove first occurrence

# Syntax: list.remove(element)
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')  # Removes first 'banana'
print(fruits)  # ['apple', 'orange', 'banana']

# Error if element not found
try:
    fruits.remove('grape')
except ValueError as e:
    print(f"Error: {e}")

# Safe removal
if 'grape' in fruits:
    fruits.remove('grape')