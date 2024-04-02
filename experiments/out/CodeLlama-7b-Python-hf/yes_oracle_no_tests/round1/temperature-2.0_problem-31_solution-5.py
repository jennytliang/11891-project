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
    
	Include these tokens in the code: n _ sqrt = 1
	"""

    if n <= 1:
        return False
    sqrt = 1
    for i in range(2, int(sqrt) + 1):
        if n % i == 0:
            return False
        sqrt = int(n ** 0.5)
    return True


#print(is_prime(3))
#print(is_prime(4))
#print(is_prime(5))
#print(is_prime(6))
#print(is_prime(7))
#print(is_prime(8))
#print(is_prime(9))
#print(is_prime(10))
#print(is_prime(11))
#print(is_prime(12))
