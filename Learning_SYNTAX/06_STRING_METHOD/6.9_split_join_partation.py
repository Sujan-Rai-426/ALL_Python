

# NOTE: split(): Splits a string into a list of substrings based on a separator (defaults to whitespace).
sentence = "apple,banana,cherry"
print(sentence.split(","))   # Output: ['apple', 'banana', 'cherry']


# NOTE: join(): Joins the elements of an iterable (like a list) into a string, using the string as a separator.
words = ["Python", "is", "awesome"]
print(" ".join(words))       # Output: Python is awesome


# NOTE: partition(): Splits the string at the first occurrence of a separator, returning a 3-tuple (before, separator, after).
text = "name=John"
print(text.partition("="))   # Output: ('name', '=', 'John')