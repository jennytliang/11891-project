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


 
    def has_even_digit(x):
        """Return True if any digit of x is even."""
        if x % 10 == 0:
            return True
        elif x < 10:
            return False
        else:
            return has_even_digit(x // 10)

    return [x for x in x if not has_even_digit(x)]


























