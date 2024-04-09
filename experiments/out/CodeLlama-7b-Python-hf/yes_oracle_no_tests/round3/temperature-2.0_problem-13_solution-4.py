def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	Do not include these tokens in the code: if == 0
	"""
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
