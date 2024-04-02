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
    
	Include these tokens in the code: def round ing ( val ):
	'''
    def rounding(value):
        number = float(value)
        return int(number + 0.5)
    return rounding(value)


if __name__ == '__main__':
    print("Example:")
    print(closest_integer('10'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert closest_integer('10') == 10
    assert closest_integer('0') == 0
    assert closest_integer('100000000000000000000000000') == 100000000000000000000000000
    assert closest_integer('-10') == -10
    assert closest_integer('-15.3') == -15
    assert closest_integer('15.3') == 15
    assert closest_integer('-14.5') == -15
    assert closest_integer('14.5') == 15
    assert closest_integer('-2.49999') == -2
    assert closest_integer('-2.5') == -3
    assert closest_integer('-2.50001') == -2
    assert closest_integer('2.5') == 3
    assert closest_integer('2.50001') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")