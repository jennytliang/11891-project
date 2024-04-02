def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""
    prime_factor = 2
    while n > 1:
        while n % prime_factor != 0:
            prime_factor += 1
        n /= prime_factor
    return prime_factor
