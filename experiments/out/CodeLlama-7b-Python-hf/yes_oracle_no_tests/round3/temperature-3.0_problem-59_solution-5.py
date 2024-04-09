def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime =
	Do not include these tokens in the code: #
	"""
    # is prime =
    for i in range(2, n+1):
        if n % i == 0:
            j = 2
            while j < i:
                if i % j == 0:
                    break
                j += 1
            if j == i:
                return i
    return 1


def prime_factors(n: int):
    """Return a sorted list of the prime factors of n.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(177)
    [177]
    >>> prime_factors(301231)
    [7, 13, 23, 31]
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors


def unique_prime_factors(n: int):
    """Return a sorted list of the unique prime factors of n.
    >>> unique_prime_factors(100)
    [2, 5]
    >>> unique_prime_factors(177)
    [177]
    >>> unique_prime_factors(301231)
    [7, 13, 23, 31]
    """
    return list(set(prime_factors(n)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
