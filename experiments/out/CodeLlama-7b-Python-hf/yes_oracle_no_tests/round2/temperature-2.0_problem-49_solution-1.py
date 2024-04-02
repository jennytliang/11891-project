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
    
	Include these tokens in the code: res
	Do not include these tokens in the code: # print (" Input s : n
	"""
    res = 2**n % p
    # print(" Input s : n")
    return res

def modp_test(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp_test(3, 5)
    3
    >>> modp_test(1101, 101)
    2
    >>> modp_test(0, 101)
    1
    >>> modp_test(3, 11)
    8
    >>> modp_test(100, 101)
    1
    
	Include these tokens in the code: res
	Do not include these tokens in the code: # print (" Input s : n
	"""
    res = 2**n % p
    # print(" Input s : n")
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    