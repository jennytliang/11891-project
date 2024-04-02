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
    # ------------------------------------------------------------------
    # TODO: 1. Replace the pass statement below with your code
    # ------------------------------------------------------------------
    pass

    # ------------------------------------------------------------------
    # TODO: 2. When you are ready to have your code checked,
    # comment out the pass statement and uncomment the other lines.
    # ------------------------------------------------------------------
    print("Standard response: ", closest_integer("10"))
    print("Standard response: ", closest_integer("15.3"))
    print("Standard response: ", closest_integer("14.5"))
    print("Standard response: ", closest_integer("-14.5"))


def main():
    """ Calls the functions in the file with different inputs. """
    print("Exercise 2: ")
    print("closest_integer('10')")
    closest_integer('10')
    print("closest_integer('15.3')")
    closest_integer('15.3')
    print("closest_integer('14.5')")
    closest_integer('14.5')
    print("closest_integer('-14.5')")
    closest_integer('-14.5')


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()