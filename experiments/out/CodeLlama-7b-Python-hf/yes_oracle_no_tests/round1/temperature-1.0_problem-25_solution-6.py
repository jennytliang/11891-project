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
    
    if n <= 0: raise ValueError('Input should be a positive integer.')
    
    import math
    primes = [2, 3]
    primeFactors = []
    while primes:
        factors = []
        i  = primes.pop(0)
        while n % i == 0:
            primes.append(i)
            factors.append(i)
            n = n // i
            
        if factors: primeFactors += factors
    
    primeFactors = primeFactors + [n]
    
    return primeFactors


def is_power2(n):
    return factorize(n)[1:] == [2]