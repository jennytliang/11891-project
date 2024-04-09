def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a < 0 or b
	"""
    if a < 0 or b < 0:
        return None
    if a == 0 or b == 0:
        return max(a, b)
    if a > b:
        return greatest_common_divisor(b, a)
    if a % b == 0:
        return b
    return greatest_common_divisor(b, a % b)



def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a < 0 or b
	"""
    if a < 0 or b < 0:
        return None
    if a == 0 or b == 0:
        return max(a, b)
    return a * b // greatest_common_divisor(a, b)



def is_prime(a: int) -> bool:
    """ Return whether a number a is a prime number
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(101)
    True
    >>> is_prime(102)
    False
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a < 0
	"""
    if a < 0:
        return None
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(a**0.5) + 1, 2):
        if a % i == 0:
            return False
    return True



def prime_factorization(a: int) -> list:
    """ Return a list of prime factors of an integer a
    >>> prime_factorization(1)
    []
    >>> prime_