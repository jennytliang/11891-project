def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    factor = 1
    while p <= n:
        if prime[p]:
            factor = p
        p += 1
    return factor


if __name__ == "__main__":
    import doctest

    doctest.testmod()
