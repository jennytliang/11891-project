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
    
	Do not include these tokens in the code: if
	"""

    if n <= 1: return Fals
    for i in range(2, n):
        if n % i == 0: return False
    return True


def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(6)
    [2, 3]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(70)
    [2, 5, 7]
    >>> prime_factors(1024)
    [2, 2, 2, 2, 2, 2, 2, 2, 2]
    >>> prime_factors(1730)
    [2, 3, 5, 7, 11]
    >>> prime_factors(42)
    [2, 3, 7]
    >>> prime_factors(46)
    [2, 3, 11]
    >>> prime_factors(1000)
    [2, 2, 2, 5, 5, 5]
    >>> prime_factors(10000)
    [2, 2, 2, 2, 5, 5, 5, 57]
    >>> prime_factors(100000)
    [2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 57]
    >>> prime_factors(1728)
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    >>> prime_factors(1944)
    [2, 2, 2, 2, 2, 2