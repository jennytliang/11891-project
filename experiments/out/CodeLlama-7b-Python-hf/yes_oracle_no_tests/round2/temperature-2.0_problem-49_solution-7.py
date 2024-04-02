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
    
	Include these tokens in the code: res ,
	"""
    res = 1
    for _ in range(n):
        res = (res * 2) % p
    return res


def modp_power(base: int, exponent: int, p: int):
    """Return base^exponent modulo p (be aware of numerics).
    >>> modp_power(3, 3, 5)
    3
    >>> modp_power(1101, 1100, 101)
    1
    >>> modp_power(3, 11, 11)
    8
    >>> modp_power(0, 100, 101)
    1
    """
    res = 1
    for _ in range(exponent):
        res = (res * base) % p
    return res


def modp_power_binary(base: int, exponent: int, p: int):
    """Return base^exponent modulo p (be aware of numerics).
    >>> modp_power_binary(3, 3, 5)
    3
    >>> modp_power_binary(1101, 1100, 101)
    1
    >>> modp_power_binary(3, 11, 11)
    8
    >>> modp_power_binary(0, 100, 101)
    1
    """
    res = 1
    while exponent > 0:
        if exponent % 2 == 1:
            res = (res * base) % p
        base = (base * base) % p
        exponent = exponent // 2
    return res


def modp_power_binary_iter(base: int, exponent: int, p: int):
    """Return base^exponent modulo p (be aware of numerics).
    >>> modp_power_binary_iter(3, 3, 5)
    3
    >>> modp_power_binary_iter(1101, 1100, 101)
    1
    >>> modp_power_binary