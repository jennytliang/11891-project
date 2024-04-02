def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""
    for i in range(2, n + 1):
        if n % i == 0:
            while n % i == 0:
                n = n / i
            if n % i != 0:
                return i


print(largest_prime_factor(13195))
print(largest_prime_factor(2048))
