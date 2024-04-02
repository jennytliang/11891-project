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
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        sqr = int(math.sqrt(n)) + 1

        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    
    result = []
    
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                if is_prime(i):
                    result.append(i)
                    n //= i
                    break
    return result