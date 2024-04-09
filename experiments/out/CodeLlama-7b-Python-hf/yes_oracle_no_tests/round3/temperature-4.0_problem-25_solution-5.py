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
    factorization = []
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factorization.append(i)
            while n % i == 0:
                n = n // i
            if n == 1:
                break
    if n != 1:
        factorization.append(n)
    return factorization


if __name__ == "__main__":
    import doctest
    doctest.testmod()
