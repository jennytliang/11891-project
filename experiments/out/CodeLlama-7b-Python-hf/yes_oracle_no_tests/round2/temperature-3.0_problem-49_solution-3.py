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
    
	Include these tokens in the code: , x
	"""

  
    return 2**n % p


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
    
	Include these tokens in the code: , x
	"""
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return (2 * modp_fast(n - 1, p)) % p


if __name__ == "__main__":
    import doctest

    doctest.testmod()