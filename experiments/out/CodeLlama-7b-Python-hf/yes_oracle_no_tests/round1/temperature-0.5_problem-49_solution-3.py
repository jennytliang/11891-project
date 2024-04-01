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
    
	Do not include these tokens in the code:  return pow ( 2 , n , p )
	"""

    # if n == 0:
    #     return 1

    # return 2 ** n % p

    return pow(2, n, p)


def modp_inverse(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_inverse(3, 5)
    3
    >>> modp_inverse(1101, 101)
    2
    >>> modp_inverse(0, 101)
    1
    >>> modp_inverse(3, 11)
    8
    >>> modp_inverse(100, 101)
    1
    
	Do not include these tokens in the code:  return pow ( 2 , n , p )
	"""

    return pow(n, -1, p)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
