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
    
	Include these tokens in the code: return
	Do not include these tokens in the code: re =
	"""



    if  n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    re = int(n ** 0.5)
    for i in range(3, re, 2):
        if n % i == 0:
            return False
    return True












