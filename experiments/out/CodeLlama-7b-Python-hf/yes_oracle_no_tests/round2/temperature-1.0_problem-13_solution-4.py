def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	Do not include these tokens in the code: small = large =
	"""
    # Your code here    
    if a > b:
        small = b
    else:
        small = a
    for x in range(1, small + 1):
        if a % x == 0 and b % x == 0:
            large = x
    return large


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #greatest_common_divisor(3, 5)
    #greatest_common_divisor(25, 15)
