def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	"""
    # [x for x in range(2, n) if (n % x == 0 and is_prime(x))]
    # for x in range(2, n):
    #     if n % x == 0 and is_prime(x):
    #         return x
    # return -1

    largest_prime = 1
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime


def is_prime(n: int):
    """Returns True if n is a prime number, False otherwise.
    >>> is_prime(3)
    True
    >>> is_prime(11)
    True
    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    >>> is_prime(12)
    False
    >>> is_prime(25)
    False
    """
    # if n < 2:
    #     return False
    # for i in range(2, n):
    #     if n % i == 0:
    #         return False
    # return True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(13195))
