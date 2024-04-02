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
    s = 2
    res = 1
    while n:
        p -= 1
        if p == 0:
            return res
        if n & 1:
            res = (res * s) % p
        s = (s * s) % p
        n >>= 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
