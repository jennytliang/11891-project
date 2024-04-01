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
    
	Include these tokens in the code:  import math  fact
	Do not include these tokens in the code: factors
	"""

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0 or n % 3 == 0:
            return False
        return all(n % i for i in range(5, int(math.sqrt(n)) + 1, 6))

    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.append(i)
                n = n // i
                break
    return factors


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
    
	Include these tokens in the code:  import math  fact
	Do not include these tokens in the code: factors
	"""
    return [i for i in range(2, n + 1) if n % i == 0]
