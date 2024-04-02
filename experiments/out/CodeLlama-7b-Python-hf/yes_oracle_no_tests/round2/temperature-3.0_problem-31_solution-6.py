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
    
	Include these tokens in the code: False n _ sqrt = 1
	Do not include these tokens in the code: F als
	"""


    if n <= 1: 
        return False
    else:
        sqrt = 1
        while sqrt*sqrt < n:
            sqrt += 1
        for i in range(2, sqrt):
            if n % i == 0:
                return False
        return True
    
    


def prime_factors(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(19)
    [19]
    >>> prime_factors(24)
    [2, 2, 2, 3]
    >>> prime_factors(25)
    [5, 5]
    >>> prime_factors(32)
    [2, 2, 2, 2, 2, 2]
    >>> prime_factors(37)
    [37]
    >>> prime_factors(40)
    [2, 2, 2, 5]
    >>> prime_factors(42)
    [2, 3, 7]
    >>> prime_factors(512)
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    """
    factors = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                factors.append(i)
                n = n/i
                break
    return factors
    


def prime_factors_alt(n):
    """Return a list of the prime factors of n.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(19)
    [19]
    >>> prime_factors(24)
    [2, 2,