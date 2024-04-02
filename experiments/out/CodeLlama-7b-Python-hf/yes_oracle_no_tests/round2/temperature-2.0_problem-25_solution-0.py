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
    result = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                result.append(i)
                break
    return result


def factorize_prime(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize_prime(8)
    [2, 2, 2]
    >>> factorize_prime(25)
    [5, 5]
    >>> factorize_prime(70)
    [2, 5, 7]
    
	Include these tokens in the code: import math
	"""
    result = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                result.append(i)
                break
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
