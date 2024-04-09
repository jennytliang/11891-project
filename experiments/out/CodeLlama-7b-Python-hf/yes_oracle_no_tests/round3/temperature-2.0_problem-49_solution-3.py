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
    # res = 2**n % p
    # x = p
    # while n > 0:
    #     res = (res * res) % x
    #     n = n // 2
    #     x = (x * x) % p
    # return res
    if n == 0:
        return 1
    elif n % 2 == 0:
        tmp = modp(n // 2, p)
        return (tmp * tmp) % p
    else:
        tmp = modp(n // 2, p)
        return (tmp * tmp * p) % p


if __name__ == "__main__":
    import doctest

    doctest.testmod()
