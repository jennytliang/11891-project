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

    return pow(2, n, p)


def modp2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp2(3, 5)
    3
    >>> modp2(1101, 101)
    2
    >>> modp2(0, 101)
    1
    >>> modp2(3, 11)
    8
    >>> modp2(100, 101)
    1
    
	Do not include these tokens in the code:  return pow ( 2 , n , p )
	"""

    return 1 if n == 0 else pow(2, n, p)


def modp3(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp3(3, 5)
    3
    >>> modp3(1101, 101)
    2
    >>> modp3(0, 101)
    1
    >>> modp3(3, 11)
    8
    >>> modp3(100, 101)
    1
    
	Do not include these tokens in the code:  return pow ( 2 , n , p )
	"""

    return 1 if n == 0 else (pow(2, n - 1, p) * 2) % p


def modp4(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp4(3, 5)
    3
    >>> modp4(1101, 101)
    2
    >>> modp4(0, 101)
    1
    >>> modp4(3, 11)
    8
    >>> modp4(100, 101)
    1
    
	Do not include these tokens in the code:  return pow ( 2 , n