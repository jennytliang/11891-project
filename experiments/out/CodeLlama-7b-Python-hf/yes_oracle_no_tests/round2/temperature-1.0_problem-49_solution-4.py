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
    return (2**n)%p


def modp_in(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_in(3, 5)
    3
    >>> modp_in(1101, 101)
    2
    >>> modp_in(0, 101)
    1
    >>> modp_in(3, 11)
    8
    >>> modp_in(100, 101)
    1
    
	Include these tokens in the code: res ,
	"""
    res = 1
    for i in range(n):
        res = modp(res, p)
    return res


def modp_out(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_out(3, 5)
    3
    >>> modp_out(1101, 101)
    2
    >>> modp_out(0, 101)
    1
    >>> modp_out(3, 11)
    8
    >>> modp_out(100, 101)
    1
    
	Include these tokens in the code: res ,
	"""
    res = 2
    for i in range(n):
        res = modp(res, p)
    return res


def modp_in_out(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_in_out(3, 5)
    3
    >>> modp_in_out(1101, 101)
    2
    >>> modp_in_out(0, 101)
    1
    >>> modp_in_out(3, 11)
    8
    >>> modp_in_out(100, 101)
    1
    
	