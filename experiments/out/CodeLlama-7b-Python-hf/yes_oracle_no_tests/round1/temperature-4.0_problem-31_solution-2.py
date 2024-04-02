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

    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factors(m):
    """Print all prime factors of a given number m.
    >>> prime_factors(100)
    2
    2
    5
    5
    >>> prime_factors(105)
    3
    5
    11
    """
    n = m
    while n > 1:
        if is_prime(n):
            print(n)
            n = n - 1
        else:
            for i in range(2, n):
                if n % i == 0 and is_prime(i):
                    print(i)
                    n = n / i
                    break
