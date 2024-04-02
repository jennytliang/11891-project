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
    #
    # The function should be called closest_integer and should take a
    # single parameter, which should be a string representing a number.
    #
    # The function should return an integer that is the closest to the
    # number represented by the string. If two integers are equally
    # close to the given number, then the function should return the
    # integer that is the farthest from zero.
    #
    # If the given string is not a valid representation of a number,
    # then the function should return None.
    #
    # Examples:
    # >>> closest_integer("10")
    # 10
    # >>> closest_integer("15.3")
    # 15
    # >>> closest_integer("14.5")
    # 15
    # >>> closest_integer("-14.5")
    # -15
    # >>> closest_integer("one hundred")
    # None
    #
    # Hint: You will need to use the built-in float() function to
    # convert the string into a number.

    # YOUR CODE HERE
    return round(float(value))