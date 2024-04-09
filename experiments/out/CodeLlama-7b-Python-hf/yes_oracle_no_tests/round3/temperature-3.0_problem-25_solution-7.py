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
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def prime_factors(n):
        result = []
        while n % 2 == 0:
            result.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                result.append(i)
                while n % i == 0:
                    n //= i
        if n > 2:
            result.append(n)
        return result

    result = []
    if is_prime(n):
        result.append(n)
    else:
        result = prime_factors(n)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
