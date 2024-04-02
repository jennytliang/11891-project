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
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: n
	"""
    res = 1
    x = 2**n
    while x <= p:
        res = (res*x) % p
        x = x*2
    return res


def modp_3(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_3(3, 5)
    3
    >>> modp_3(1101, 101)
    2
    >>> modp_3(0, 101)
    1
    >>> modp_3(3, 11)
    8
    >>> modp_3(100, 101)
    1
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: n
	"""
    res = 1
    x = 2**n
    while x <= p:
        res = (res*x) % p
        x = x*2
    return res


def modp_4(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_4(3, 5)
    3
    >>> modp_4(1101, 101)
    2
    >>> modp_4(0, 101)
    1
    >>> modp_4(3, 11)
    8
    >>> modp_4(100, 101)
    1
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: n
	"""
    res = 1
    x = 2**n
    while x <= p:
        res = (res*x) % p
        x = x*2
    return res


def modp_5(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_5(3, 5)
    3
    >>> modp_5