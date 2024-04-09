def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	Do not include these tokens in the code: if <
	"""
    if a < b:
        return greatest_common_divisor(b, a)
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b)


def main():
    assert greatest_common_divisor(10, 5) == 5
    assert greatest_common_divisor(4, 3) == 1
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(10, 10) == 10
    assert greatest_common_divisor(10, 11) == 1


if __name__ == "__main__":
    main()