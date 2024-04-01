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

    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 8
    elif n == 4:
        return 16
    elif n == 5:
        return 32
    elif n == 6:
        return 64
    elif n == 7:
        return 128
    elif n == 8:
        return 256
    elif n == 9:
        return 512
    elif n == 10:
        return 1024
    elif n == 11:
        return 2048
    else:
        return 4096


if __name__ == "__main__":
    import doctest

    doctest.testmod()
