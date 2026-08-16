# Example 1: Simple counter
# NOTE: DO WHILE LOOP ALWAYS EXECUTE ONCE EVEN IF CONDITION IS SATISFIED OR NOT
counter = -1
while True:
    print(f"Count: {counter}")
    counter -= 1
    
    if counter < 0:  # Exit condition
        break
# Output: Count: -1