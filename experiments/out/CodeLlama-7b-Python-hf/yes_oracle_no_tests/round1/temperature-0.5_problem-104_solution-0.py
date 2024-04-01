def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code:  def judge ( x ): 
	"""

    # The algorithm should be a one-liner.
    # You should use set comprehension.
    # You should use the function int(x).
    # You should use the function str(x).
    # You should use the function set().
    # You should use the function sum().
    # You should use the function any().
    # You should use the function all().
    # You should use the function sorted().

    return sorted({x for x in x if not any(int(i) % 2 == 0 for i in str(x))})



def unique_digits2(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code:  def judge ( x ): 
	"""

    # The algorithm should be a one-liner.
    # You should use set comprehension.
    # You should use the function int(x).
    # You should use the function str(x).
    # You should use the function set().
    # You should use the function sum().
    # You should use the function any().
    # You should use the function all().
    # You should use the function sorted().

    return sorted({x for x in x if not any(int(i) % 2 == 0 for i in str(x))})



def unique_digits3(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422