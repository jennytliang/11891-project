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
    assert type(n) == int and n > 0
    primes = [2, 3, 5]
    n = [2, 3, 5]
    l = 0
    while n[l] * n[l] <= primes[-1]:
        if not any(map(lambda prime: prime % n[l] == 0, list(range(2, n[l])))) and n[l] != n[l - 1]:
            primes.append(n[l])
        l += 1
