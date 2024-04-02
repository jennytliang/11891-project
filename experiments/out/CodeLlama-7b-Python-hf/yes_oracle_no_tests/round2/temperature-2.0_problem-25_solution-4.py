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
        if n % 2 == 0:
            n /= 2
            result.append(2)
        else:
            factor = 3
            while factor * factor <= n:
                if n % factor == 0:
                    n /= factor
                    result.append(factor)
                    break
                factor += 2
            else:
                result.append(int(n))
                break
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
