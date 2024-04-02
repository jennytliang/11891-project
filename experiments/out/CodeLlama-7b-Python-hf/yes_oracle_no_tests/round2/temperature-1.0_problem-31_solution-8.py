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
    if n == 2:
        return True
    sqrt = 1
    for _ in range(2, n+1):
        sqrt += 1
        if n % sqrt == 0:
            return False
    else:
        return True 
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()