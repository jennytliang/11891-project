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
    res = x = n
    while x > 0:
        if x % 2 == 1:
            res = (res + p) % p
        x = x // 2
    return res


def modp_alt(n: int, p: int):
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
    res = x = n
    while x > 0:
        if x % 2 == 1:
            res = (res + p) % p
        x = x // 2
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
