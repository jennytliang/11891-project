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
    
    prime_factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            prime_factors.append(divisor)
            n = n / divisor
            divisor = 2
        else:
            divisor += 1
    return prime_factors


def check_correctness(n: int, expected: List[int]) -> bool:
    for item in expected:
        print(n * item == factorize(n * item))
        if n * item != factorize(n * item):
            return False
    return True


# print(factorize(5))
# print(factorize(4))

print(check_correctness(5, [1, 5]))
print(check_correctness(7, [7]))
print(check_correctness(12, [2, 2, 3]))
print(check_correctness(4, [2, 2]))