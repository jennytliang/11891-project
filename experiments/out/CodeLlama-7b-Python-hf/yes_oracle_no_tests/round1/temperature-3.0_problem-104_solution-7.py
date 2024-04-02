def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: judge
	Do not include these tokens in the code: has _ even _ digit
	"""


 
    # =============================================================================
    # My Solution
    # =============================================================================
    # def unique_digits(x):
    #     """Given a list of positive integers x. return a sorted list of all 
    #     elements that hasn't any even digit.
    # 
    #     Note: Returned list should be sorted in increasing order.
    #     
    #     For example:
    #     >>> unique_digits([15, 33, 1422, 1])
    #     [1, 15, 33]
    #     >>> unique_digits([152, 323, 1422, 10])
    #     []
    #     
    #      Include these tokens in the code: judge
    #      Do not include these tokens in the code: has _ even _ digit
    #      """
    #     return sorted([int(x) for x in list(str(y)) if int(x) % 2 != 0])


    # =============================================================================
    # More Pythonic Solution
    # =============================================================================
    return sorted(map(int, filter(lambda x: int(x) % 2 != 0, list(map(str, x)))))