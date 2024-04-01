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

    def is_prime(n: int) -> bool:
        """ Return True if n is prime. """
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        d = 5

        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
            if n % d == 0:
                return False
            d += 4

        return True

    def get_prime_factors(n: int, prime_factors: List[int]) -> List[int]:
        """ Add to prime_factors all prime factors of n. """
        d = 2
        while d * d <= n:
            while n % d == 0:
                prime_factors.append(d)
                n //= d
            d += 1
        if n > 1:
            prime_factors.append(n)
        return prime_factors

    if n < 2:
        return []

    prime_factors = []
    get_prime_factors(n, prime_factors)

    return prime_factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
