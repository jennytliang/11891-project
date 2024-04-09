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

    def rounding(value):
        return int(round(float(value)))

    def closest_integer(value):
        return rounding(value)

    return closest_integer(value)


def test_function():
    assert closest_integer('10') == 10, "First"
    assert closest_integer('15.3') == 15, "Second"
    assert closest_integer('14.5') == 15, "Third"
    assert closest_integer('-14.5') == -15, "Fourth"
    assert closest_integer('-14.4') == -15, "Fifth"
    assert closest_integer('14.6') == 15, "Sixth"
    assert closest_integer('2.49') == 2, "Seventh"
    assert closest_integer('2.5') == 3, "Eighth"
    assert closest_integer('2.50') == 2, "Ninth"
    assert closest_integer('-2.49') == -2, "Tenth"
    assert closest_integer('-2.50') == -2, "Eleventh"
    assert closest_integer('2.499999999999999') == 2, "Twelfth"
    assert closest_integer('2.5000000000000001') == 3, "Thirteenth"


if __name__ == '__main__':
    test_function()
