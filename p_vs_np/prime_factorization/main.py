import math

def prime_factors(n):
    factors = []
    
    # Step 1: Divide n by 2 as many times as possible
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Step 2: Check for odd factors from 3 up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # Step 3: If n is still greater than 2, it's prime
    if n > 2:
        factors.append(n)
        
    return factors
