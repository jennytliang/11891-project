from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    
	Include these tokens in the code: import math
	"""
    factors = []
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:
    """ Return True if given integer is a prime number, False otherwise.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(7)
    True
    >>> is_prime(121)
    False
    >>> is_prime(919)
    True
    """
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> prime_factorize(8)
    [2, 2, 2]
    >>> prime_factorize(25)
    [5, 5]
    >>> prime_factorize(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
            while n % i == 0:
                n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
