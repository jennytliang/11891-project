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
    
	Include these tokens in the code: <=  1 : return False  n _
	Do not include these tokens in the code: <
	"""

    if n  <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def is_prime2(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime2(6)
    False
    >>> is_prime2(101)
    True
    >>> is_prime2(11)
    True
    >>> is_prime2(13441)
    True
    >>> is_prime2(61)
    True
    >>> is_prime2(4)
    False
    >>> is_prime2(1)
    False
    """

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime3(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime3(6)
    False
    >>> is_prime3(101)
    True
    >>> is_prime3(11)
    True
    >>> is_prime3(13441)
    True
    >>> is_prime3(61)
    True
    >>> is_prime3(4)
    False
    >>> is_prime3(1)
    False
    """

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime4(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime4(6)
    False
    >>> is_prime4(101)
    True
    >>> is_prime4(11)
    True
    >>> is_prime4(13441)
    True
    >>> is_prime4(61)
    True
    >>> is_prime