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
        return []
    res = []
    while n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                n //= i
                res.append(i)
                break
        else:
            res.append(n)
            n = 1
    return res
    



import math


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
        return []
    res = []
    while n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                n //= i
                res.append(i)
                break
        else:
            res.append(n)
            n = 1
    return res





























































































































































