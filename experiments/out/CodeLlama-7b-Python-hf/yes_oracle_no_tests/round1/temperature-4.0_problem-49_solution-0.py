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
    for i in range(1, n + 1):
        res = (res * 2) % p
    return res


def modp_naive(n: int, p: int):
    """Return 2^n modulo p (naive implementation).
    >>> modp_naive(3, 5)
    3
    >>> modp_naive(1101, 101)
    2
    >>> modp_naive(0, 101)
    1
    >>> modp_naive(3, 11)
    8
    >>> modp_naive(100, 101)
    1
    """
    return pow(2, n, p)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
