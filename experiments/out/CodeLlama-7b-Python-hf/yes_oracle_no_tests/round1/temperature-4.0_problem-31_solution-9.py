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
    "*** YOUR CODE HERE ***"
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True


def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(20)
    [2, 5]
    >>> prime_factors(25)
    [5]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(11)
    [11]
    """
    "*** YOUR CODE HERE ***"
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors


def prime_factors_mult(n):
    """Return the product of all the prime factors of n.
    >>> prime_factors_mult(8)
    8
    >>> prime_factors_mult(20)
    10
    >>> prime_factors_mult(25)
    5
    >>> prime_factors_mult(12)
    12
    >>> prime_factors_mult(11)
    11
    """
    "*** YOUR CODE HERE ***"
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors[0] * factors[1]


def unique_