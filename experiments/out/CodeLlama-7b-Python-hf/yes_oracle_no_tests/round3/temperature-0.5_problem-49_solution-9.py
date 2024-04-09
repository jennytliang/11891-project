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
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: =
	"""

  
    # =============================================================================
    # The following function is provided for your use.
    #
    # def power(x, y):
    #     if y == 0:
    #         return 1
    #     elif y == 1:
    #         return x
    #     else:
    #         return x * power(x, y - 1)
    # =============================================================================

    if n == 0:
        return 1
    elif n == 1:
        return p
    else:
        return power(p, n) % p


if __name__ == "__main__":
    import doctest

    doctest.testmod()
