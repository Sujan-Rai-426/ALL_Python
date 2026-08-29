def fibonacci_recursive(n):
    """Fibonacci using recursion (inefficient for large n)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """Fibonacci using iteration (efficient)"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms"""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

# Test
print(f"10th Fibonacci: {fibonacci_iterative(10)}")
print(f"First 10 Fibonacci numbers: {fibonacci_sequence(10)}")