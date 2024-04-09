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
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:
    """ Return True if the given number is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    
	Include these tokens in the code: import math
	"""
    if n < 2:
        return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))


def count_primes(n: int) -> int:
    """ Return the number of prime numbers in the range 1 to n.
    >>> count_primes(1)
    0
    >>> count_primes(2)
    1
    >>> count_primes(3)
    2
    >>> count_primes(6)
    3
    >>> count_primes(10)
    4
    
	Include these tokens in the code: import math
	"""
    c = 0
    for i in range(1, n):
        if is_prime(i):
            c += 1
    return c


def count_primes_v2(n: int) -> int:
    """ Return the number of prime numbers in the range 1 to n.
    >>> count_primes_v2(1)
    0
    >>> count_primes_v2(2)
    1
    >>> count_primes_v2(3)
    2
    >>> count_primes_v2(6)
    3
    >>> count_primes_v2(10)
    4
    
	Include these tokens in the code: import math
	"""
    c