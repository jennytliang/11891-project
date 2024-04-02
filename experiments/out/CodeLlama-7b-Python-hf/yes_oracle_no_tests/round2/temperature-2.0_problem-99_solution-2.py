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
    
	Include these tokens in the code: val
	Do not include these tokens in the code: value
	'''

    def roun(num):
        return int(num + 0.5)

    def roun2(num):
        return int(num - 0.5)

    def roun3(num):
        return int(num + 0.5) if num - int(num) == 0.5 else int(num - 0.5)

    val = float(value)
    res = roun(val)
    res2 = roun2(val)
    res3 = roun3(val)
    return max([res, res2, res3], key=abs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
