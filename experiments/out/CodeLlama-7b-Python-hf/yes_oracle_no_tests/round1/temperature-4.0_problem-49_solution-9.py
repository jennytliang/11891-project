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


def modp_rec(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
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
	Include these tokens in the code: res , x =
    """
    if n == 0:
        return 1
    else:
        return (2 * modp_rec(n - 1, p)) % p


if __name__ == "__main__":
    import doctest
    doctest.testmod()
