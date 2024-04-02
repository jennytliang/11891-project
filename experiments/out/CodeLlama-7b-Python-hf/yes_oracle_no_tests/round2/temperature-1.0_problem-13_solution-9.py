def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	Do not include these tokens in the code: while
	"""
    if a == b: 
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    else:
        return greatest_common_divisor(a, b - a)


def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(2, 3)
    6
    >>> least_common_multiple(2, 3)
    6
    
	Include these tokens in the code: def query _ l cm ( a : int ,
	Do not include these tokens in the code: while
	"""
    return a * b // greatest_common_divisor(a, b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
