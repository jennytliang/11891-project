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
    
	Include these tokens in the code: res , x =
	"""
    x = 1
    res = 1
    while(x < n):
        x = x + 1
        res = (res * 2) % p
    return res


def modp_fast(n: int, p: int):
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
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    while(n > 0):
        if n % 2 == 1:
            res = (res * 2) % p
        n = n // 2
    return res


def modp_fast_2(n: int, p: int):
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
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    while(n > 0):
        if n % 2 == 1:
            res = (res * res) % p
        n = n // 2
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
