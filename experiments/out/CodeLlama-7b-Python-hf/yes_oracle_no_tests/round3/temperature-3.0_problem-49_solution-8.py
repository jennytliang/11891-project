def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    
	Include these tokens in the code: , x
	"""

  
    i = 0
    while (i < n):
        if (i == 0):
            x = 2
        else:
            x = x * 2 % p
        i = i + 1
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()