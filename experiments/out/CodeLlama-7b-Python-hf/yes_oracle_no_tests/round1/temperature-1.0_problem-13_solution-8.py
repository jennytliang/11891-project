def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	"""

    if a == 0 and b == 0: return None
    if a == 0: return b
    if b == 0: return a
    
    # a < b: (a, b) -> (b, a)
    # a > b: (a, b) -> (a - b, b)
    if a > b:
        a, b = b, a
        
    # (a - b) < a
    while (a - b) < a:
        a -= b # a <= a - b < a -> a - b < a
        
    # a = a - b
    if a < 0: return None
    
    return a