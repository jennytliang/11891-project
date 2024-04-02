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
    res = x = 1
    for i in range(n):
        res = (x*x) % p
        x = res
    return res


def modp_rec(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
	Recursive version.
    >>> modp_rec(3, 5)
    3
    >>> modp_rec(1101, 101)
    2
    >>> modp_rec(0, 101)
    1
    >>> modp_rec(3, 11)
    8
    >>> modp_rec(100, 101)
    1
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: n
	"""
    if n == 0:
        return 1
    else:
        res = x = 1
        for i in range(n):
            res = (x*x) % p
            x = res
        return res


def modp_while(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
	While version.
    >>> modp_while(3, 5)
    3
    >>> modp_while(1101, 101)
    2
    >>> modp_while(0, 101)
    1
    >>> modp_while(3, 11)
    8
    >>> modp_while(100, 101)
    1
    
	Include these tokens in the code: res , x
	Do not include these tokens in the code: n
	"""
    res = x = 1
    while n > 0:
        res = (x*x) % p
        x = res
        n -= 1
    return res


def modp_for(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
	For version.
   