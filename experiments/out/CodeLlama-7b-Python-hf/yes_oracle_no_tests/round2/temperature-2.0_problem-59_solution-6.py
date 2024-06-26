def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	"""
    for i in range(3, n // 2, 2):
        if n % i == 0:
            for j in range(2, i // 2):
                if i % j == 0:
                    break
            else:
                return i
