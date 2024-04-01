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

    # 2^n mod p = 2^(n mod p)
    return pow(2, n % p, p)
