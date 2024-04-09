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
    res = 1
    x = 2
    while x <= n:
        if x % p == 0:
            res = (res * 2) % p
        x = (x * 2) % p
    return res


def modp_faster(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_faster(3, 5)
    3
    >>> modp_faster(1101, 101)
    2
    >>> modp_faster(0, 101)
    1
    >>> modp_faster(3, 11)
    8
    >>> modp_faster(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    x = 2
    while x <= n:
        if x % p == 0:
            res = (res * 2) % p
        x = (x * 2) % p
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
