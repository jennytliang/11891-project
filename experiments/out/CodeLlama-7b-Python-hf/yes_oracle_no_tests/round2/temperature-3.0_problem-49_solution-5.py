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
    
	Include these tokens in the code: res ,
	"""
    res = 1
    for i in range(n):
        res = (res * 2) % p
    return res


def modp_power(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_power(3, 5)
    3
    >>> modp_power(1101, 101)
    2
    >>> modp_power(0, 101)
    1
    >>> modp_power(3, 11)
    8
    >>> modp_power(100, 101)
    1
    
	Include these tokens in the code: res ,
	"""
    res = 1
    while n > 0:
        if n & 1:
            res = (res * p) % p
        p = (p * p) % p
        n >>= 1
    return res


def modp_power_2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_power_2(3, 5)
    3
    >>> modp_power_2(1101, 101)
    2
    >>> modp_power_2(0, 101)
    1
    >>> modp_power_2(3, 11)
    8
    >>> modp_power_2(100, 101)
    1
    
	Include these tokens in the code: res ,
	"""
    res = 1
    while n > 0:
        if n & 1:
            res = (res * p) % p
        n >>= 1
        p = (p * p) % p
    return res


def modp_power_3(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_power_3(3, 5)
    3
    >>> modp