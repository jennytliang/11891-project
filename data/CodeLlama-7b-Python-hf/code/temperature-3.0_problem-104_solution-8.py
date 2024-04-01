def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def has_even_digit(x):
        """Given a list of positive integers x. return True if and only if x 
        has an even digit."""
        for digit in map(int, str(x)):
            if not digit % 2: return True
        return False