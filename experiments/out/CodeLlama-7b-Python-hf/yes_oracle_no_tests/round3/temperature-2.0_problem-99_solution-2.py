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
    
	Include these tokens in the code: round ing
	Do not include these tokens in the code: r oun
	'''


 
    # your code here
    import math
    def rounding(value):
        if value % 1.0 == 0.5:
            return int(value) + 1
        elif value % 1.0 == 0.5:
            return int(value)
        else:
            return round(value)
    return rounding(float(value))


if __name__ == '__main__':
    print("Example:")
    print(closest_integer('10'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert closest_integer('10') == 10
    assert closest_integer('0') == 0
    assert closest_integer('-10') == -10
    assert closest_integer('15.3') == 15
    assert closest_integer('14.5') == 15
    assert closest_integer('-14.5') == -15
    assert closest_integer('14.4999') == 14
    assert closest_integer('-14.4999') == -14
    assert closest_integer('14.5001') == 15
    assert closest_integer('-14.5001') == -15
    assert closest_integer('14.45') == 14
    assert closest_integer('-14.45') == -14
    assert closest_integer('14.55') == 15
    assert closest_integer('-14.55') == -15
    assert closest_integer('14.449999999999999') == 14
    assert closest_integer('-14.449999999999999') == -14
    assert closest_integer('14.550000000000001') == 15
    assert closest_integer('-14.550000000000001') == -1