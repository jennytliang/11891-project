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
    while i < n:
        if i == 0:
            r = 2
        else:
            r = r * 2
        r = r % p
        i += 1
    return r


print(modp(100, 101))