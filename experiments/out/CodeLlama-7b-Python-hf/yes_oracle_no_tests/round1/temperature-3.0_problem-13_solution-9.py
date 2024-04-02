def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	"""
    
    return a if a == b or a == 1 or b == 1 else greatest_common_divisor(b, a % b)

def main():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    main()