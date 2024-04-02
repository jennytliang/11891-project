def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: min ( b
	"""

    if a > b:
        a, b = b, a
    return [i for  i in range(a, b+1) if i % 2 == 0]


def test_function():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 14) == [2, 4, 6, 8, 10, 12, 14]
    assert generate_integers(0, 1) == []
    assert generate_integers(100, 100) == [100]
    assert generate_integers(100, 101) == [100, 101]
    assert generate_integers(101, 100) == [100, 101]
    assert generate_integers(101, 102) == [102]
    assert generate_integers(102, 101) == [101, 102]

if __name__ == '__main__':
    test_function()
