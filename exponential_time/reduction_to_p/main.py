def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Initialize the starting values
    grandparent = 0
    parent = 1
    current = 1
    
    # Loop to calculate Fibonacci values up to the nth index
    for _ in range(n - 1):
        # Calculate the next Fibonacci number
        current = parent + grandparent
        # Update grandparent and parent for the next iteration
        grandparent = parent
        parent = current

    return current
