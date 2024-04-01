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
    if n <= 0:
        raise ValueError("Input number should be a positive number")

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return prime_factors


import math

if __name__ == "__main__":
    print(factorize(8))
    print(factorize(25))
    print(factorize(70))
