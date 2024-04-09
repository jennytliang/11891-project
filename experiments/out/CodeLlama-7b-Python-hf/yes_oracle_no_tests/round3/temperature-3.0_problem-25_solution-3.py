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
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n = n // i
    if n != 1:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:
    """ Return True if given number is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    >>> is_prime(3244)
    False
    >>> is_prime(2147483647)
    False
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def is_perfect(n: int) -> bool:
    """ Return True if given number is a perfect number, False otherwise.
    A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(14)
    False
    >>> is_perfect(27)
    False
    """
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum += i
    return sum == n


def is_abundant(n: int) -> bool:
    """ Return True if given number is abundant, False otherwise.
    A number is abundant if the sum of its proper divisors is greater than the