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
    if (n == 0):
        return 1
    if (n == 1):
        return 2
    # split n in odd/even part wrt. binary representation
    x = (n >> 1)
    r = (n & 1)
    # modp(2*odd, odd) == mod(p,odd)+mod(p,odd)
    res = 2 * (modp(x, p))
    if (r == 0):
        # even number
        # result fits between 0 and p-1
        # return remainder
        return ((res < p) and res or res - p) % p
    elif (p % 4 == (res - (p >> 2) * (r % 2) + ((p >> 1) << 1)) % p):
        res = (res - p) % p
    else:
        res = (2*((p >> 1) + (r >> 1) + (r & 1)))
    if (res < (p >> 1)):
        return res
    else:
        return -(p - res)


    
    
