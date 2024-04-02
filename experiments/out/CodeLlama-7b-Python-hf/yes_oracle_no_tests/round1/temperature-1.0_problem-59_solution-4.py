def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, n + 1):
        if prime[i] == True:
            for j in range(2, n // i + 1):
                prime[i * j] = False
    for i in range(n, 0, -1):
        if prime[i] == True:
            return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
