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
    if n == 0:
        return 1
    x = 2
    for i in range(n - 1):
        x = (x * 2) % p
    return x


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
    while n > 0:
        if n % 2 == 1:
            res = res * 2 % p
        n = n // 2
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
