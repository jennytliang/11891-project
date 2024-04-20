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
    while True:
        res = pow(x, n, p)
        if res == 1:
            break
        if res == p - 1:
            break
        x += 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()