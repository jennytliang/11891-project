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
    """
    return pow(2, n, p)


def modp_inv(n: int, p: int):
    """Return 2^(-n) modulo p (be aware of numerics).
    >>> modp_inv(3, 5)
    3
    >>> modp_inv(1101, 101)
    2
    >>> modp_inv(0, 101)
    1
    >>> modp_inv(3, 11)
    8
    >>> modp_inv(100, 101)
    1
    """
    return pow(2, -n, p)


def modp_inv2(n: int, p: int):
    """Return 2^(-n) modulo p (be aware of numerics).
    >>> modp_inv2(3, 5)
    3
    >>> modp_inv2(1101, 101)
    2
    >>> modp_inv2(0, 101)
    1
    >>> modp_inv2(3, 11)
    8
    >>> modp_inv2(100, 101)
    1
    """
    return pow(2, -n, p)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

