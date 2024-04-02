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
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    if n % 3 == 0:
        return [3] + factorize(n // 3)
    if n % 5 == 0:
        return [5] + factorize(n // 5)
    if n % 7 == 0:
        return [7] + factorize(n // 7)
    if n % 11 == 0:
        return [11] + factorize(n // 11)
    if n % 13 == 0:
        return [13] + factorize(n // 13)
    if n % 17 == 0:
        return [17] + factorize(n // 17)
    if n % 19 == 0:
        return [19] + factorize(n // 19)
    if n % 23 == 0:
        return [23] + factorize(n // 23)
    if n % 29 == 0:
        return [29] + factorize(n // 29)
    if n % 31 == 0:
        return [31] + factorize(n // 31)
    if n % 37 == 0:
        return [37] + factorize(n // 37)
    if n % 41 == 0:
        return [41] + factorize(n // 41)
    if n % 43 == 0:
        return [43] + factorize(n // 43)
    if n % 47 == 0:
        return [47] + factorize(n // 47)
    if n % 53 == 0:
        return [53] + factorize(n // 53