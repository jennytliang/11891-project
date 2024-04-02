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
    if n < 1:
        raise ValueError('factorize() accepts only natural numbers')

    def is_prime(num):
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """ Return list of prime numbers that divide n. """
        primes = [2]
        for i in range(3, n + 1, 2):
            if is_prime(i):
                primes.append(i)
        return primes

    def get_factorization(n, primes):
        """ Return list of prime factors of n. """
        if n == 1:
            return []
        for prime in primes:
            if n % prime == 0:
                return [prime] + get_factorization(n // prime, primes)
        raise ValueError(f'{n} is not a product of prime numbers')

    return get_factorization(n, get_primes(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
