def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: False n _ sqrt = 1
	Do not include these tokens in the code: F als
	"""


    if n <= 1: 
        return False
    elif n <= 3:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        else:
            return True


def prime_factors(n):
    """Return a list of the prime factors of a number.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(7)
    [7]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(33)
    [3, 11]
    >>> prime_factors(225)
    [5, 5, 5]
    >>> prime_factors(20)
    [2, 2, 5]
    >>> prime_factors(21)
    [3, 7]
    
	Include these tokens in the code: n _
	Do not include these tokens in the code:
    """

    factors = []
    while n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                factors.append(i)
                n = n // i
                break
        else:
            factors.append(n)
            n = 1
    return factors


def prime_factors_mult(n):
    """Return the product of all the prime factors of a number.
    >>> prime_factors_mult(10)
    10
    >>> prime_factors_mult(12)
    6
    >>> prime_factors_mult(13441)
    13441
    >>> prime_factors_mult(125)
    125
    >>> prime_factors_mult(124)
    24
    >>> prime_factors_mult(101)
    101
    >>> prime_factors_mult(13441)
    13441
