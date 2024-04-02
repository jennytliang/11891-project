def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    
	Include these tokens in the code: def round ing ( val ): if abs
	'''
    # pass
    # Write your code here
    return int(round(float(value)))


def test_cases():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("-14.4") == -15
    assert closest_integer("-14.6") == -15
    assert closest_integer("1234.5") == 1235
    assert closest_integer("-1000.5") == -1000
    assert closest_integer("5.55") == 6
    assert closest_integer("5.45") == 5
    assert closest_integer("5.455") == 5
    assert closest_integer("5.55") == 6
    assert closest_integer("5.65") == 6
    assert closest_integer("5.655") == 6


if __name__ == '__main__':
    test_cases()
