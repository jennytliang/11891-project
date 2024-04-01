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
    
	Include these tokens in the code: n _ sqrt = 1 while n
	Do not include these tokens in the code: #
	"""


    if n  <= 1:
        r = False
    elif n == 2:
        r = True
    elif n % 2 == 0:
        r = False
    else:
        sqrt = int(n ** 0.5) + 1
        for i in range(3, sqrt, 2):
            if n % i == 0:
                r = False
                break
            else:
                r = True
    return r


def prime_factors(n):
    """Return a sorted list of the prime factors of n.
    >>> prime_factors(20)
    [2, 5]
    >>> prime_factors(81)
    [3, 3, 3, 3]
    >>> prime_factors(12)
    [2, 2, 3]
    
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)

            while n % i == 0:
                n //= i
        i += 1
    if n != 1:
        factors.append(n)
    return factors


def largest_prime_factor(n):
    """Return the largest prime factor of n.
    >>> largest_prime_factor(10)
    5
    >>> largest_prime_factor(187)
    73
    >>> largest_prime_factor(10000)
    251
    
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
        i += 1
    return n


def prime_factors_mult(n):
    """Return a sorted list of the prime factors of n.
    >>> prime_factors_mult(20)
    5
    >>> prime_factors_mult(187)
    73
    >>> prime_factors_mult(10000)
    251
    
    """
    i = 2
