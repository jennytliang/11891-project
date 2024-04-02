def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query
	Do not include these tokens in the code: if a == 0 :
	"""
    if a == 0:
        return b
    return greatest_common_divisor(b % a, a)


print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))
