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
    for i in range(n):
        res = (res * 2) % p
    return res


def modp_fast(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_fast(3, 5)
    3
    >>> modp_fast(1101, 101)
    2
    >>> modp_fast(0, 101)
    1
    >>> modp_fast(3, 11)
    8
    >>> modp_fast(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    for i in range(n):
        res = (res * 2) % p
    return res


def modp_fastest(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_fastest(3, 5)
    3
    >>> modp_fastest(1101, 101)
    2
    >>> modp_fastest(0, 101)
    1
    >>> modp_fastest(3, 11)
    8
    >>> modp_fastest(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    res = 1
    for i in range(n):
        res = (res * 2) % p
    return res


def modp_fastestest(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_fastestest(3, 5)
    3
    >>> modp_fastestest(1101, 101)
    2
    >>> modp_fastestest(0, 101)
    1
    >>> modp_fastestest(3,