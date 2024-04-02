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
    import math
    if float(value) == math.floor(float(value)):
        return int(float(value))
    elif float(value) > 0:
        return int(math.ceil(float(value)))
    else:
        return int(math.floor(float(value)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
