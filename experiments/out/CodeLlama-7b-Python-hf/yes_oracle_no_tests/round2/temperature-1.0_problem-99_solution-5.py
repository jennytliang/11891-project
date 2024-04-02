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

    def round_away_from_zero(value):
        """Rounds the given number away from zero.

        A number is considered equally distance from 0 if the magnitude of
        the difference equals the magnitude of the difference with the next
        integer. E.g. 77.0 and 77.5 are equally distance from 0.

        >>> round_away_from_zero(76.5)
        77
        >>> round_away_from_zero(77.5)
        78
        """
        float_val = float(value)
        int_val = int(float_val)
        return int_val + (abs(float_val - int_val) >= 0.5)

    try:
        val = float(input(value))
        return round_away_from_zero(val)
    except Exception:
        return input


print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))
