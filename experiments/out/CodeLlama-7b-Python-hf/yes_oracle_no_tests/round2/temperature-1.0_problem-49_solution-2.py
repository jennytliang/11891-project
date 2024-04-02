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
    return (pow(2, n, p) + p) % p


def modp_2(n: int, p: int):
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
    res = 1
    while n:
        if n & 1:
            res = (res * 2) % p
        n //= 2
    return res


def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    assert modp(100, 11) == 1
    assert modp(100, 111) == 1
    assert modp(100, 1111) == 1
    assert modp(100, 11111) == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
