def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    for candidate in reversed(range(2, n + 1)):
        if n % candidate == 0:
            is_prime = True
            for j in range(2, candidate):
                is_prime &= candidate % j != 0 
            if is_prime: 
                return candidate