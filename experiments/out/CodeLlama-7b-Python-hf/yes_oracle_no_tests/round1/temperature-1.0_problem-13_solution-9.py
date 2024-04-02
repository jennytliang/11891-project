def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	"""
    if a < b:
        smaller = a
    else:
        smaller = b

    gcd = 1
    for i in range(2, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
            pass
    return gcd
