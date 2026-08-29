
#NOTE: Syntax: list.extend(iterable)
fruits = ['apple', 'banana']
fruits.extend(['orange', 'mango'])
print(fruits)  # ['apple', 'banana', 'orange', 'mango']

# Extend with string (adds each character)
letters = ['a', 'b']
letters.extend('cd')  # ['a', 'b', 'c', 'd']

# Extend with tuple
numbers = [1, 2]
numbers.extend((3, 4))  # [1, 2, 3, 4]

# Difference between extend and append
list1 = [1, 2]
list1.append([3, 4])  # [1, 2, [3, 4]]
list2 = [1, 2]
list2.extend([3, 4])  # [1, 2, 3, 4]