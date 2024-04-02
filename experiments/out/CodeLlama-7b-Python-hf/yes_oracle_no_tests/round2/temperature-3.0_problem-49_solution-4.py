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

  
    return (2**n) % p


def modp_2(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_2(3, 5)
    3
    >>> modp_2(1101, 101)
    2
    >>> modp_2(0, 101)
    1
    >>> modp_2(3, 11)
    8
    >>> modp_2(100, 101)
    1
    """

    # your code here
    if n == 0:
        return 1
    else:
        return (2 * modp_2(n-1, p)) % p


def modp_3(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_3(3, 5)
    3
    >>> modp_3(1101, 101)
    2
    >>> modp_3(0, 101)
    1
    >>> modp_3(3, 11)
    8
    >>> modp_3(100, 101)
    1
    """

    # your code here
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (modp_3(n/2, p) ** 2) % p
    else:
        return (modp_3(n/2, p) ** 2 * 2) % p


def modp_4(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_4(3, 5)
    3
    >>> modp_4(1101, 101)
    2
    >>> modp_4(0, 101)
    1
    >>> modp_4(3, 11)
    8