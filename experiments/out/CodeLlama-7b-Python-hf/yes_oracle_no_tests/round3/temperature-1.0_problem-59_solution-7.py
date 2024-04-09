def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    
    m = n
    while m > 1 and not primes[m]:
        m -= 1
    return m


if __name__ == "__main__":
    import doctest
    doctest.testmod()