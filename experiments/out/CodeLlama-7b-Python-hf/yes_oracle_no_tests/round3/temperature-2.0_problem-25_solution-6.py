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
    factor = 2
    while n > 1:
        if n % factor == 0:
            result.append(factor)
            n /= factor
        else:
            factor = int(math.sqrt(n)) + 1
            if factor * factor > n:
                result.append(n)
                break
    return result
