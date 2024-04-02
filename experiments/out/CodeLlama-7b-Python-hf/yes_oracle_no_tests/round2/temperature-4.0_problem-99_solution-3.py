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
    # return int(round(float(value)))
    if abs(float(value) - int(value)) == 0.5:
        return int(value) + 1
    else:
        return int(value)


if __name__ == '__main__':
    print('Example:')
    print(closest_integer('10'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert closest_integer('-123') == -123
    assert closest_integer('123') == 123
    assert closest_integer('123.5') == 124
    assert closest_integer('-123.5') == -124
    assert closest_integer('123.49999999999999') == 123
    assert closest_integer('10000.5') == 10001
    assert closest_integer('-10000.5') == -10001
    assert closest_integer('123.499999999999999') == 124
    print('Wow, you are doing pretty good. Time to check it!')
