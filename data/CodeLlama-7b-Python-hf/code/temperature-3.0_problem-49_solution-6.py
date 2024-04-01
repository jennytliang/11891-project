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
    """
    return pow(2, n, p)


def modp_inv(n: int, p: int):
    """Return 2^(-1) modulo p.
    >>> modp_inv(3, 5)
    3
    >>> modp_inv(1101, 101)
    12
    >>> modp_inv(0, 101)
    1
    >>> modp_inv(3, 11)
    8
    >>> modp_inv(100, 101)
    2
    """
    return pow(2, -1, p)


def modp_exp(n: int, e: int, p: int):
    """Return (2^n)**e modulo p (be aware of numerics). Use modular exponentiation: 2^n (mod p) is
    equal to (2^(2^(n/2)))^2 (mod p). This is more efficient for large n.
    """
    if n < 0:
        raise ValueError("Cannot calculate (2^n)^e as n < 0.")
    if n == 0:
        return 1
    return (
        pow(modp(n // 2, p), 2, p) if n % 2 == 0 else pow(modp(n, p), e, p)
    )
