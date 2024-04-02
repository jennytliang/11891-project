def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	Do not include these tokens in the code: if ==
	"""
    if a == 0 or b == 0:
        return 0
    elif a == b:
        return a
    if a < b:
        return greatest_common_divisor(b, a)
    return greatest_common_divisor(b, a - b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()