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
    
	Include these tokens in the code: n _ sqrt = 1
	"""

    if n <= 1:
        return False
    sqrt = 1
    for i in range(2, n):
        if n % i == 0:
            sqrt += 1
    return sqrt == 1


def is_prime_2(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_2(6)
    False
    >>> is_prime_2(101)
    True
    >>> is_prime_2(11)
    True
    >>> is_prime_2(13441)
    True
    >>> is_prime_2(61)
    True
    >>> is_prime_2(4)
    False
    >>> is_prime_2(1)
    False
    
	Include these tokens in the code: n _ sqrt = 1
	"""
    if n <= 1:
        return False
    sqrt = 1
    for i in range(2, n):
        if n % i == 0:
            sqrt += 1
    return sqrt == 1
