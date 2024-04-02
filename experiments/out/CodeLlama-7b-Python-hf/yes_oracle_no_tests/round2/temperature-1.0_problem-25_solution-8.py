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
    
    # We take the same principle as with the Sieve of Eratosthenes. 
    # So, first we eliminate all of the positive divisors of the number than can be written form 2*i+1 where  i is a natural number, 
    prime_factors = []
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if is_prime[i] == True:  # i is prime
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    for i in range(2, n + 1):
        if is_prime[i] == True:  # i is prime
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            prime_factors.append(i)
            if count != 0:
                prime_factors.append(count)    
                
    return prime_factors

def factorize_all(n: int) -> List[List[int]]:
    """ Write a function that takes an integer number (n) and returns all possible factorizations of this number 
    as a list of lists

>>> factorize_all(32)
[[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [2, 4, 4], [2, 4, 2, 2], [4, 4, 4], [4, 8]]
    
    >>> factorize_all(12)
    [[2, 2, 6], [2, 2, 2, 3], [2, 3, 4], [3, 4, 2], [2, 6], [3, 6], [2, 2, 2, 3], [2, 2, 3,