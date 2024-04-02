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
    # res = 1
    # x = 1
    # while x <= n:
    #     if x % p == 0:
    #         res = (res * 2) % p
    #     x = x + 1
    # return res
    res = 1
    x = 1
    while x <= n:
        if x % p == 0:
            res = (res * 2) % p
        else:
            res = (res * 2 * x) % p
        x = x + 1
    return res


def modp2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp2(3, 5)
    3
    >>> modp2(1101, 101)
    2
    >>> modp2(0, 101)
    1
    >>> modp2(3, 11)
    8
    >>> modp2(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    x = 1
    while x <= n:
        if x % p == 0:
            res = (res * 2) % p
        else:
            res = (res * (2 * x) % p)
        x = x + 1
    return res


def modp3(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp3(3, 5)
    3
    >>> modp3(1101, 101)
    2
    >>> modp3(0, 101)
    1
    >>> modp3(3, 11)
    8
    >>> modp3(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    x = 1
    while