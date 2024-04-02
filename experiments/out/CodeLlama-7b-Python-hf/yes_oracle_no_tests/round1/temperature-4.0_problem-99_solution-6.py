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

    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------


########################################################################
# The TEST functions for the  above function are located in
# m4e_closest_integer.py
#
# After implementing this TEST function, proceed to m4e.py.
########################################################################

def main():
    """ Calls the TEST functions. """
    run_test_closest_integer()


# To allow calling the main function from the command line,
# uncomment the following line.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()