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
    return int(round(float(value)))


def test_cases():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("-14.4999999999999") == -15
    assert closest_integer("14.4999999999999") == 15
    assert closest_integer("1234.5") == 1235
    assert closest_integer("-1000") == -1000
    assert closest_integer("55.499999999999") == 56
    assert closest_integer("-55.499999999999") == -56
    assert closest_integer("-55.5") == -55
    assert closest_integer("55.5") == 56
    assert closest_integer("0.4999999999999") == 0
    assert closest_integer("-0.4999999999999") == 0
    assert closest_integer("-0.5") == 0
    assert closest_integer("0.5") == 1


def run_test():
    test_cases()
    print("Test Success!")


run_test()
