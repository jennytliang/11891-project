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
    # factorize(n: int) -> List[int]:
    # raise NotImplementedError()
    factors = []
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()