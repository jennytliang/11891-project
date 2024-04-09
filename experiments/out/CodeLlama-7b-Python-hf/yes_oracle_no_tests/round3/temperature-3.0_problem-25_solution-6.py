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
    import math

    def is_prime(num):
        if num == 2 or num == 3:
            return True
        if num < 2 or num % 2 == 0 or num % 3 == 0:
            return False
        return all(num % i for i in range(5, int(math.sqrt(num)) + 1, 6))

    def get_prime_factors(n):
        prime_factors = []
        while n % 2 == 0:
            prime_factors.append(2)
            n /= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                prime_factors.append(i)
                n /= i
        if n > 2:
            prime_factors.append(int(n))
        return prime_factors

    prime_factors = get_prime_factors(n)
    return prime_factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
