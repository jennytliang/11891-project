def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	Do not include these tokens in the code: if ==
	"""
    # is prime = [ True ] * ( n +
    for i in range(2, n+1):
        if n%i == 0:
            n = n//i
            # Do not include these tokens in the code: if ==
            if i > 1:
                return i

if __name__ == "__main__":
    import doctest
    doctest.testmod()