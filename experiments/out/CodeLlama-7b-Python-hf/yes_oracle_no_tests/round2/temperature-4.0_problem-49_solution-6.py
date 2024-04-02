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

  
    if n == 0:
        return 1
    else:
        return (2**n) % p

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

    return (2**n) % p


def modp_fastest(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_fastest(3, 5)
    3
    >>> modp_fastest(1101, 101)
    2
    >>> modp_fastest(0, 101)
    1
    >>> modp_fastest(3, 11)
    8
    >>> modp_fastest(100, 101)
    1
    
	Include these tokens in the code: , x
	"""

    return (2**n) % p


def modp_fastest2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_fastest2(3, 5)
    3
    >>> modp_fastest2(1101, 101)
    2
    >>> modp_fastest2(0, 101)
    1
    >>> modp_fastest2(3, 11)
    8
    >>> modp_fastest2(100, 101)
    1
    
	Include these tokens in the code: , x
	"""

