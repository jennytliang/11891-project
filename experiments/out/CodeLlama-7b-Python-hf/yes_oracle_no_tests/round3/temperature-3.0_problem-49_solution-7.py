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
    while n > 0:
        if (n & 1) != 0:
            res = (res * x) % p
        x = (x * x) % p
        n >>= 1
    return res


def modp_2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_2(3, 5)
    3
    >>> modp_2(1101, 101)
    2
    >>> modp_2(0, 101)
    1
    >>> modp_2(3, 11)
    8
    >>> modp_2(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    x = 1
    res = 1
    while n > 0:
        if (n & 1) != 0:
            res = (res * x) % p
        x = (x * x) % p
        n >>= 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
