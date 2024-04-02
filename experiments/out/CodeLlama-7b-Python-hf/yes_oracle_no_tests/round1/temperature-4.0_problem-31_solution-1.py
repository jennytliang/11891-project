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
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(11)
    [11]
    >>> prime_factors(15)
    [3, 5]
    >>> prime_factors(61)
    [1, 61]
    >>> prime_factors(13441)
    [1, 13441]
    >>> prime_factors(10**10)
    [1, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    
	Include these tokens in the code: while n > 2
    """
    factors = []
    if n <= 1:
        return factors
    if n == 2:
        return [2]
    if n % 2 == 0:
        factors.append(2)
        n = n / 2
    while n > 2:
        for i in range(3, n + 1, 2):
            if n % i == 0:
                factors.append(i)
                n = n / i
                break
    factors.append(int(n))
    return factors


def prime_factorization(n):
    """Return a dictionary containing the prime factors and
    their multiplicities of n.
    >>> prime_factorization(10)
    {2: 1, 5: 1}
    >>> prime_factorization(11)
    {11: 1}
    >>> prime_factorization(15)
    {3: 1, 5: 1}
    >>> prime_factorization(13441)
    {11: 2, 13: 2}
    >>> prime_