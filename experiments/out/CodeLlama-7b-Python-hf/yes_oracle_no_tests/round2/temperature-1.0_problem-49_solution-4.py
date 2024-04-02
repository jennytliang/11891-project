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
    # res = (-1) ** ((-1 * n) // (p - 1))
    # res *= 2 ** (n % (p - 1))
    # return res
    # # return modulo(2**(n % (p-1)))
    return modulo(3 ** n)


# DO NOT CHANGE THIS FUNCTION    
def modulo(n):
    s = str(bin(n))[2:]  # to string without 0b
    s = s[::-1]  # reverse the result
    s = s.replace("0", "")  # replace zeros
    s = s.replace("1", "3")
    s = s.replace("2", "1")
    s = s.replace("3", "0")
    s = int(s[::-1], 2)  # reverse back
    s = s % 101
    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
