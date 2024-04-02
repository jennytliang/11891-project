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
    sqrt = int(n ** 0.5) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True


def is_prime_v2(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_v2(6)
    False
    >>> is_prime_v2(101)
    True
    >>> is_prime_v2(11)
    True
    >>> is_prime_v2(13441)
    True
    >>> is_prime_v2(61)
    True
    >>> is_prime_v2(4)
    False
    >>> is_prime_v2(1)
    False
    
	Include these tokens in the code: n _ sqrt = 1
	"""

    if n <= 1:
        return False
    sqrt = int(n ** 0.5) + 1
    for i in range(2, sqrt):
        if n % i != 0:
            continue
        else:
            return False
    return True


def is_prime_v3(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime_v3(6)
    False
    >>> is_prime_v3(101)
    True
    >>> is_prime_v3(11)
    True
    >>> is_prime_v3(13441)
    True
    >>> is_prime_v3(61)
    True
    >>> is_prime_v3(4)
    False
    >>> is_prime_v3(1)
    False
    
	Include these tokens in the code: n _ sqrt = 1
	"""

    if n <= 1:
        return False
    sqrt = int(n ** 0.5) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False