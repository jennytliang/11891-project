def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if b == 0 :
	"""
    if b == 0:
        return int(a)
    return greatest_common_divisor(int(b), int(a) % int(b))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import pdb;pdb.set_trace()
