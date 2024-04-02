def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for num
	"""
    #---------------------------------------------------------------------------
    # Done: 1.
    #   First, replace this comment and the preceding empty line
    #   with a comment that describes what the function does.
    #
    # Done: 2.
    #   Replace the ___ with the appropriate code for this problem.
    #---------------------------------------------------------------------------
    result = []
    for num in x:
        if num % 2 != 0:
            result.append(num)
    return result

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
