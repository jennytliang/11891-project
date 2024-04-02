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
    
	Do not include these tokens in the code: # - * - coding : utf
	'''

    # Your code here
    def closest_integer(value):
        return round(float(value))
    return closest_integer(value)


if __name__ == '__main__':
    print('Example:')
    print(closest_integer('10'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert closest_integer('10') == 10
    assert closest_integer('0') == 0
    assert closest_integer('1000') == 1000
    assert closest_integer('-1000') == -1000
    assert closest_integer('543.321') == 543
    assert closest_integer('-543.321') == -543
    assert closest_integer('123.329') == 123
    assert closest_integer('-123.329') == -123
    assert closest_integer('123.330') == 123
    assert closest_integer('-123.330') == -123
    assert closest_integer('100.5') == 101
    assert closest_integer('-100.5') == -101
    print('Wow, you are doing pretty good. Time to check it!')
