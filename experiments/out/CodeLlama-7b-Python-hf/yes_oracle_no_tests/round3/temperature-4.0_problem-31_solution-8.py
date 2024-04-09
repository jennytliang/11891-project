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
    
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    if n <= 1:
        return False
    for i in range(2, n+1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(6)
    [2, 3]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(15)
    [3, 5]
    >>> prime_factors(17)
    [17]
    >>> prime_factors(111)
    [11, 11]
    >>> prime_factors(199)
    [199]
    """
    result = []
    for i in range(2, n+1):
        if is_prime(i) and n % i == 0:
            result.append(i)
    return result

def prime_factors_mult(n):
    """Return a list of the prime factors of n, but each element should
    appear as many times as its multiplicity.
    >>> prime_factors_mult(6)
    [2, 2, 3]
    >>> prime_factors_mult(101)
    [101]
    >>> prime_factors_mult(12)
    [2, 2, 3]
    >>> prime_factors_mult(15)
    [3, 5]
    >>> prime_factors_mult(17)
    [17]
    >>> prime_factors_mult(111)
    [11, 11]
    >>> prime_factors_mult(199)
    [199]
    """
    result = []
    for i in range(2, n+1):
        if is_prime(i) and n % i == 0:
            result.append(i)
            n = n / i
            while