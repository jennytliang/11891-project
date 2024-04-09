def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i, n + 1, i):
                prime[j] = False
    return [i for i in range(2, n + 1) if prime[i] and n % i == 0][-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
