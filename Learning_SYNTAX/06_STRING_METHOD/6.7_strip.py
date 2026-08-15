
# NOTE: strip(): Removes leading and trailing whitespace (or specified characters).
# NOTE: lstrip() and rstrip(): Removes whitespace only from the left or right side respectively.

text = "   Hello Python!   "

print(text.strip())          # Output: Hello Python!

new_text = "---Python---"
print(new_text.strip("-"))       # Output: Python
print(new_text.lstrip("-"))      # Output: Python---
print(new_text.rstrip("-"))      # Output: ---Python