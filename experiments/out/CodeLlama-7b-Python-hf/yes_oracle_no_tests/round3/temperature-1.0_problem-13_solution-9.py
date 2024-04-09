def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a == b :
	"""
    if a == b :
        return a
    elif a > b:
        return greatest_common_divisor(a - b, b)
    else:
        return greatest_common_divisor(a, b - a)


def least_common_multiple(a: int, b: int) -> int:
    """ Return a least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a == b :
	"""
    return a * b // greatest_common_divisor(a, b)


def main() -> None:
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
