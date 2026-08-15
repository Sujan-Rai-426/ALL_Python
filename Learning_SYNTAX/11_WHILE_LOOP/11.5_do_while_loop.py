# Example 1: Simple counter
counter = 0
while True:
    counter += 1
    print(f"Count: {counter}")
    
    if counter >= 5:  # Exit condition
        break
# Output: Count: 1, 2, 3, 4, 5