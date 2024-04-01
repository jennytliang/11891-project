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
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def prime_factors(n):
    """Return a list of the prime factors of the positive integer n.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(17)
    [17]
    >>> prime_factors(45)
    [3, 5]
    >>> prime_factors(66)
    [2, 3, 11]
    >>> prime_factors(123456789)
    [7, 13, 29]
    >>> prime_factors(4)
    [2, 2]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(16)
    [2, 2, 2, 2]
    >>> prime_factors(1000)
    [2, 2, 2, 5, 5, 5]
    >>> prime_factors(10000000)
    [2, 5, 5, 5, 5, 5, 5, 5]
    >>> prime_factors(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    [2, 3, 3, 3, 3, 5, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59