def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = []
	"""

  
    # --------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   The testing code is already written for you (above).
    #
    # Note: 4-step process
    #   Step 1:  READ the above specification and change the parameter n to
    #            n+1 so that it is odd.
    #   Step 2:  READ the above specification and understand it.
    #   Step 3:  IMPLEMENT and test the above specification.
    #   Step 4:  READ the above specification and change the parameter n to
    #            n+1 so that it is even.
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # --------------------------------------------------------------------------

    a_list = []
    for k in range(n):
        if n % 2 == 1:
            n = n + 2
            a_list.append(n)
        else:
            n = n + 1
            a_list.append(n)
    return a_list


























































































































































































