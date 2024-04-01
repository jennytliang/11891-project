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
    x = 2
    res = 1
    for i in range(n):
        res = (res*x) % p
        x = (x*x) % p
    return res


def modp_inv(n: int, p: int):
    """Return multiplicative inverse of n modulo p.
    >>> modp_inv(3, 5)
    2
    >>> modp_inv(1101, 101)
    5
    >>> modp_inv(0, 101)
    1
    >>> modp_inv(3, 11)
    7
    """
    return modp(n, p)


def modp_pow(a: int, n: int, p: int):
    """Return a^n modulo p (be aware of numerics).
    >>> modp_pow(3, 3, 5)
    3
    >>> modp_pow(1101, 1101, 101)
    1
    >>> modp_pow(3, 0, 11)
    1
    >>> modp_pow(3, 3, 11)
    8
    """
    x = a
    res = 1
    for i in range(n):
        res = (res*x) % p
        x = (x*x) % p
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
