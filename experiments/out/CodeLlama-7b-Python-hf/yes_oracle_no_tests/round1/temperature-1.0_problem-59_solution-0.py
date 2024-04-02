def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    for i in range(2, n + 1): # i in P(n)

        # if ( p is True and i % p == 0 and p^2 <= n):
        if (True and i % i == 0 and i % i <= n):
            return i
        
    raise ValueError("This is not a positive integer or composite number, check your code")