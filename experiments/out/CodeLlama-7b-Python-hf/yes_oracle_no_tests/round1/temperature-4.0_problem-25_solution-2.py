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
    if n == 1:
        return [1]
    factors = []

    def is_prime(num):
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True

    def get_factors(num):
        if is_prime(num):
            factors.append(num)
            return
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
                get_factors(int(num / i))
                break

    get_factors(n)
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
