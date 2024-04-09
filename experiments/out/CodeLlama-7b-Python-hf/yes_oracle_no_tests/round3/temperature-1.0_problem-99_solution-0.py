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

    # assert isinstance(value, str)
    # assert isinstance(value, int)

    # if isinstance(value, str):
    #     value = float(value)

    # if isinstance(value, int):
    #     value = float(value)

    assert isinstance(value, (int, float))

    return round(value)


def main():
    print(closest_integer(10))
    print(closest_integer(15.3))
    print(closest_integer(-14.5))


if __name__ == '__main__':
    main()
