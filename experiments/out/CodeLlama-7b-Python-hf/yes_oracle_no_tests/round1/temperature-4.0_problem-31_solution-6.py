def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: if n <=
	"""

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(102)
    [2, 51]
    >>> prime_factors(103)
    [103]
    >>> prime_factors(104)
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    >>> prime_factors(105)
    [3, 5, 5]
    >>> prime_factors(106)
    [2, 3, 3, 3, 7]
    """

    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n = n / i
                break
    return factors
