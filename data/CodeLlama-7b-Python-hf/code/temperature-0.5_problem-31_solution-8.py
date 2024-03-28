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
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """Return a list of all prime factors of a given number.
    >>> prime_factors(6)
    [2, 3]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(11)
    [11]
    >>> prime_factors(13441)
    [17, 241]
    >>> prime_factors(61)
    [61]
    >>> prime_factors(4)
    [2, 2]
    >>> prime_factors(1)
    [1]
    """
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
                n = n / i
                break
    return factors
