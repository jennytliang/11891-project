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
    if n < 2:
        return []
    factorization = []
    while n % 2 == 0:
        n = n // 2
        factorization.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            factorization.append(i)
    if n > 2:
        factorization.append(n)
    return factorization


if __name__ == "__main__":
    import doctest

    doctest.testmod()
