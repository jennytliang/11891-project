def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    for i in range(2, 1 + int(n ** .5)):
        while n % i == 0:
            n //= i
            if i > 2:
                is_prime[i] = False
    return n
    
