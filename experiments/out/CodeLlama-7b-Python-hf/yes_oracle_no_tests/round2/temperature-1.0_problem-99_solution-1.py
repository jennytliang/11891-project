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
    # =============================================================================
    # The first line where you create a variable, and assign it a value that is
    # based on the string parameter.
    # =============================================================================
    num = float(value)
 
    # =============================================================================
    # A conditional statement controls which of the above actions will run, 
    # depending on whether or not value is a negative number.
    # =============================================================================
    if num < 0:
        if ((num + 0.5) % 1) == 0:         
            # Do the math if you need to and use the .round() function to round positive values up, negative values down
            return int(num - 0.5)             # This line of code rounds off the .5 decimal places of the returned number
        else:
            return int(num)
         
    else:
        
        if ((num - 0.5) % 1) == 0:
            return int(num + 0.5)             # This line of code rounds of the .5 decimal places of the returned number
        else:
            return int(num)
    

# 0-16
assert closest_integer("0.1"), 0
assert closest_integer("1.2"), 1
assert closest_integer("2.4"), 2
assert closest_integer("3.5"), 4
assert closest_integer("4.5"), 4
assert closest_integer("5.5"), 6
assert closest_integer("6.6"), 6

# 17-2
assert closest_integer("17.3"), 17
assert closest_integer("18.3"), 18
assert closest_integer("19.2"), 19

# 20-0
assert closest_integer("20.1"), 20
assert closest_integer("21.1"), 21
assert closest_integer("22.1"), 22
assert closest_integer("23.1"), 23
assert closest_integer("24.1"), 24
assert closest_integer("25