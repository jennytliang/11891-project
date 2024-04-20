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
    if value == '':
        return None
    else:
        return round(float(value))

def test_cases():
    assert closest_integer('10') == 10
    assert closest_integer('15.3') == 15
    assert closest_integer('14.5') == 15
    assert closest_integer('-14.5') == -15
    assert closest_integer('12.5') == 13
    assert closest_integer('-12.5') == -13
    assert closest_integer('-12.6') == -13
    assert closest_integer('12.6') == 13
    assert closest_integer('12.45') == 12
    assert closest_integer('12.455') == 13
    assert closest_integer('12.4555') == 12
    assert closest_integer('-12.4555') == -13
    assert closest_integer('12.45555') == 12
    assert closest_integer('-12.45555') == -13
    assert closest_integer('-12.455555') == -13
    assert closest_integer('12.455555') == 12
    assert closest_integer('-12.455555') == -13
    assert closest_integer('12.4555555') == 13
    assert closest_integer('-12.4555555') == -13
    assert closest_integer('-12.45555555') == -13
    assert closest_integer('12.45555555') == 13
    assert closest_integer('-12.455555555') == -13
    assert closest_integer('12.455555555') == 13
    assert closest_integer('-12.455555555