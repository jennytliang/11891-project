def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # for i in range(2, int(n**0.5)+1):
    #     if n % i == 0:
    #         if is_prime(i):
    #             return i
    # return n

    # for i in range(2, int(n**0.5)+1):
    #     if n % i == 0:
    #         if is_prime(i):
    #             return i
    # return n

    # for i in range(2, int(n**0.5)+1):
    #     if n % i == 0:
    #         if is_prime(i):
    #             return i
    # return n

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if is_prime(i):
                return i
    return n


def is_prime(n: int):
    """Return whether n is prime.
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    >>> is_prime(77)
    True
    >>> is_prime(31)
    True
    >>> is_prime(47)
    True
    >>> is_prime(23)
    False
    >>> is_prime(47)
    True
    >>> is_prime(87)
    False
    >>> is_prime(121)
    False
    >>> is_prime(131)
    False
    >>> is_prime(377)
    False
    >>> is_prime(11)
    False
    """
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def is_prime(n: int):
    """Return whether n is prime.
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    >>> is_prime(77)
    True
    >>> is_prime(31)
   