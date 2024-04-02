def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a
	Do not include these tokens in the code: [ Y OUR CO DE H
	"""
def gcd(a,b):
    assert isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)) and a > 0 and b > 0
    while a > 0 and b > 0:
        if a < b:
            a, b = b, a

        a = a - b
        
    return abs(a + b)

print(gcd(28, 48))

