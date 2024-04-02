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
	Do not include these tokens in the code: result = [] for
	"""

    # ==========================================================================
    # METHOD 1:
    # ==========================================================================
    # result = []
    # for i in x:
    #     if not(any(i % j == 0 for j in range(2,10,2))):
    #         result.append(i)

    # return sorted(result)

    # ==========================================================================
    # METHOD 2:
    # ==========================================================================
    # result = []
    # for i in x:
    #     if not(any(i % j == 0 for j in range(2,10,2))):
    #         result.append(i)

    # return sorted(result)

    # ==========================================================================
    # METHOD 3:
    # ==========================================================================
    return sorted(list(filter(lambda x: not(any(x % j == 0 for j in range(2, 10, 2))), x)))


# =============================================================================
# Start of the Code
# =============================================================================
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # print(unique_digits([15, 33, 1422, 1]))
    # print(unique_digits([152, 323, 1422, 10]))
