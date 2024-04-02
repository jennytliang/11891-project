def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd
	Do not include these tokens in the code: assert a > 0
	"""
    for number in range(min(a, b), 0, -1):
        if a % number == 0 and b % number == 0:
            return number
    if a == b:
        return a
