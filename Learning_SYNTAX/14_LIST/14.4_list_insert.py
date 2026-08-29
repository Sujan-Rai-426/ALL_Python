# NOTE: Syntax: list.insert(index, element)
fruits = ['apple', 'banana', 'orange']
fruits.insert(1, 'mango')
print(fruits)  # ['apple', 'mango', 'banana', 'orange']

# Insert at beginning
fruits.insert(0, 'grape')  # ['grape', 'apple', 'mango', 'banana', 'orange']

# Insert at end (same as append)
fruits.insert(len(fruits), 'kiwi')