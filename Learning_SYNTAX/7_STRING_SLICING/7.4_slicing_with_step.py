text = "Hello World"

# Step parameter
print(text[0:11:2])  # "HloWrd" - every 2nd character
print(text[::2])     # "HloWrd" - every 2nd character from start
print(text[::3])     # "HlWl"   - every 3rd character
print(text[1:10:2])  # "el ol"  - every 2nd from index 1 to 9