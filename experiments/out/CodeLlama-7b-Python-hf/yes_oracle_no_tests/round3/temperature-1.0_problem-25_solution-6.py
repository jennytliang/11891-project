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
    res = []
    if n <= 0:
        return res
    while n % 2 == 0:
        res.append(2)
        n //= 2
    if n == 1:
        return res
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            res.append(i)
            n //= i
        if n == 1:
            return res
    res.append(n)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
