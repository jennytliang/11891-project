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
    x = n
    res = 1
    while x > 0:
        if (x % 2) == 1:
            res = (res * p) % 101
        p = (p * p) % 101
        x = x // 2
    return res


def modp_factorial(n: int, p: int):
    """Return n! modulo p (be aware of numerics).
    >>> modp_factorial(3, 5)
    6
    >>> modp_factorial(1101, 101)
    6
    >>> modp_factorial(0, 101)
    1
    >>> modp_factorial(3, 11)
    46
    >>> modp_factorial(100, 101)
    1
    
	Include these tokens in the code: res , x =
	"""
    x = n
    res = 1
    while x > 0:
        res = (res * modp(x, p)) % p
        x = x - 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
