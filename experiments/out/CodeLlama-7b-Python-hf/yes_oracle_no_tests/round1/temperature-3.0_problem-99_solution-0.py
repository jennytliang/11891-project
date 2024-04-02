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

assert(closest_integer("10") == 10)
assert(closest_integer("15.3") == 15)
assert(closest_integer("14.5") == 15)
assert(closest_integer("-14.5") == -15)
assert(closest_integer("-14.4") == -15)
assert(closest_integer("-14.6") == -15)
assert(closest_integer("-14.45") == -15)
assert(closest_integer("-14.55") == -15)
assert(closest_integer("-14.65") == -15)
assert(closest_integer("-14.449999999999999") == -15)
assert(closest_integer("-14.450000000000001") == -15)
assert(closest_integer("-14.550000000000001") == -15)
assert(closest_integer("-14.650000000000001") == -15)
