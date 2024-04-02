def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    num = n
    i = 2
    while i <= num:
        if num % i == 0:
            num = num / i
            i = 2
        i += 1
    return i - 1


def smallest_prime_factor(n: int):
    """Return the smallest prime factor of n. Assume n > 1 and is not a prime.
    >>> smallest_prime_factor(13195)
    1989
    >>> smallest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    num = n
    i = 2
    while i <= num:
        if num % i == 0:
            num = num / i
            i = 2
        i += 1
    return i - 1


def is_prime(n: int):
    """Returns True if n is prime, False otherwise.
        >>> is_prime(2)
        True
        >>> is_prime(13195)
        False
        >>> is_prime(2048)
        True
        >>> is_prime(2**1279-1)
        True
    """
    "*** YOUR CODE HERE ***"
    num = n
    i = 2
    while i <= num:
        if num % i == 0:
            num = num / i
            i = 2
        i += 1
    if n == 1:
        return False
    else:
        return True


def prime_factors(n: int):
    """Returns a sorted list of the prime factors of n.
    >>> prime_factors(202)
    [2, 11, 17]
    >>> prime_factors(1001)
    [7, 11, 13, 17, 19, 31, 61]
    >>> prime_