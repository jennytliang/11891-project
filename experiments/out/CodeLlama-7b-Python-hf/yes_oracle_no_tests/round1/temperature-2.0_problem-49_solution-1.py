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
    # print("Inputs: n = ", n, "p = ", p)
    res = 1
    x = 2 ** n % p
    if x == 0:
        res = 1
    else:
        res = x
    # print("res = ", res)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
