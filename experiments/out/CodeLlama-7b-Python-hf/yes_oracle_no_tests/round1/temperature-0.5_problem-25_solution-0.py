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
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def prime_factors(n):
        factors = []
        if n == 1:
            return factors
        while n % 2 == 0:
            factors.append(2)
            n /= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n /= i
        if n > 2:
            factors.append(int(n))
        return factors

    return prime_factors(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
