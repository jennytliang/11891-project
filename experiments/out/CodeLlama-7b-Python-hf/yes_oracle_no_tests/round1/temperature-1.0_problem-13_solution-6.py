def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	"""
    
    assert a > 0 and b > 0 and isinstance(a, int) and isinstance(b, int)
    if a == b:
        return a
    tmp = max(a,b)
    a = min(a,b)
    b = max(a,b)
    while tmp % a:
        tmp = tmp % a
    return a


print (greatest_common_divisor.__doc__)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
