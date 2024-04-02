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
    
	Include these tokens in the code: fact
	Do not include these tokens in the code: ret
	"""

    import mat
    import numpy as np
    import math

    def fact(n):
        if n == 1:
            return np.array([1])
        elif n == 2:
            return np.array([2])
        else:
            for i in range(int(math.sqrt(n)), 1, -1):
                if n % i == 0:
                    return np.concatenate((np.array([i]), fact(n // i)))
            return np.array([n])

    return fact(n).tolist()


print(factorize(8))
