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
    """Return a list of the prime factors of a given number.
    >>> prime_factors(6)
    [2, 3]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(103)
    [103]
    >>> prime_factors(104)
    [2, 2, 2, 2, 2]
    >>> prime_factors(102)
    [2, 2, 2, 101]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(13)
    [13]
    >>> prime_factors(16)
    [2, 2, 2, 2]
    >>> prime_factors(17)
    [17]
    >>> prime_factors(18)
    [2, 3, 3]
    >>> prime_factors(19)
    [19]
    >>> prime_factors(21)
    [3, 7]
    >>> prime_factors(22)
    [2, 11]
    >>> prime_factors(26)
    [2, 13]
    """
    factors = []

    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)

    return factors


def prime_factors_2(n):
    """Return a list of the prime factors of a given number.
    >>> prime_factors_2(6)
    [2, 3]
    >>> prime_factors_2(101)
    [101]
    >>> prime_factors_2(103)
    [10