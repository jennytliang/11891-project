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
    # Implementation with prime factorization
    # from math import sqrt
    #
    # def is_prime(x):
    #     if x == 2 or x == 3: return True
    #     if x % 2 == 0 or x % 3 == 0: return False
    #     p = 5
    #     while p ** 2 <= x:
    #         if x % p == 0:
    #             return False
    #         p += 2
    #     return True
    #
    # def prime_factors(n):
    #     factors = []
    #     while n % 2 == 0:
    #         factors.append(2)
    #         n //= 2
    #     for i in range(3, int(sqrt(n)) + 1, 2):
    #         while n % i == 0:
    #             factors.append(i)
    #             n //= i
    #     if n > 2:
    #         factors.append(n)
    #     return factors
    #
    # return prime_factors(n)

    # Implementation with prime sieve
    from math import sqrt

    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    def prime_factors(n):
        factors = []
        for i in range(2, n + 1):
            if sieve[i] and n % i == 0:
                factors.append(i)
        return factors

    return prime_factors(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
