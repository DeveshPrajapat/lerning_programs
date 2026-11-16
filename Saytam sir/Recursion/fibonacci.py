def fibonacci(n):
    """nth fibonacci Numbers """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(f"Fibonacci Sequences {fibonacci(7)}") 
print(f"Fibonacci Sequences {fibonacci(4)}") 