text = "Hello World"

# Negative indices count from end
print(text[-5:])     # "World"  - last 5 characters
print(text[:-6])     # "Hello"  - all except last 6
print(text[-5:-1])   # "Worl"   - from -5 to -2
print(text[-5:11])   # "World"  - from -5 to end