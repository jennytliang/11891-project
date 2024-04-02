def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	"""

    smaller = a if a < b else b
    
    for i in range(1, smaller+1):
        if a % i == b % i and i % a == i % b:
            return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
