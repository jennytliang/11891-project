def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""

    # Your code here
    # 1. Start with 2 as factor
    # 2. Divide n by factor until n % factor != 0
    # 3. Increment factor by 1
    # 4. Return factor
    factor = 2
    while n % factor != 0:
        factor += 1
    return factor


print(largest_prime_factor(13195))
print(largest_prime_factor(2048))
print(largest_prime_factor(13195))
print(largest_prime_factor(2048))
