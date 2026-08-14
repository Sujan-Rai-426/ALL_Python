text = "Hello World"

# Empty slices
print(text[5:5])     # "" - empty (start == end)
print(text[10:5])    # "" - start > end (with positive step)

# Out of range indices
print(text[0:100])   # "Hello World" - end beyond length
print(text[-100:5])  # "Hello" - start before beginning
print(text[100:])    # "" - start beyond length

# Step with negative values
print(text[10:0:-2]) # "drWol" - reverse with step 2
print(text[5:0:-1])  # " olle" - reverse from 5 to 1