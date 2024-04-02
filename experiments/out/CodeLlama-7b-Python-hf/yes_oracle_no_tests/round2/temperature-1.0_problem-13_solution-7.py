def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Do not include these tokens in the code: return int ( abs ( b )
	"""
    if b == 0:
        return a
    a %= b
    return greatest_common_divisor(b, a)
# -------------- TESTS ----------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    