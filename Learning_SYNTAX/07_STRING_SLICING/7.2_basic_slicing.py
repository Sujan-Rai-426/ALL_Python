text = "Hello World"


print(text[0:5])     # "Hello"  - indices 0 to 4
print(text[6:11])    # "World"  - indices 6 to 10
print(text[0:11])    # "Hello World" - full string

print(text[:5])      # "Hello"  - start defaults to 0
print(text[6:])      # "World"  - end defaults to length
print(text[:])       # "Hello World" - full copy