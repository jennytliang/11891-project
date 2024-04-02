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
    import math
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def prime_factors(n):
    """Return a list of the prime factors of a given number.
    >>> prime_factors(101)
    [101]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(25)
    [5, 5]
    >>> prime_factors(32)
    [2, 2, 2, 2, 2]
    >>> prime_factors(80)
    [2, 2, 2, 5]
    >>> prime_factors(97)
    [97]
    >>> prime_factors(102)
    [2, 2, 51]
    >>> prime_factors(45)
    [3, 3, 5]
    
	Include these tokens in the code: while n > 1
	and n % i == 0
	"""
    factors = []
    i = 2
    while n > 1 and n % i == 0:
        factors.append(i)
        n /= i
        i += 1
    if n > 2:
        factors.append(n)
    return factors


def prime_factors_2(n):
    """Return a list of the prime factors of a given number.
    >>> prime_factors_2(101)
    [101]
    >>> prime_factors_2(12)
    [2, 2, 3]
    >>> prime_factors_2(25)
    [5, 5]
    >>> prime_