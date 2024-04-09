def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Do not include these tokens in the code: judge whether x has any even
	"""


    def judgement(x):
        if x % 2 == 0:
            return True
        else:
            return False

    def unique_digits_helper(x):
        if x == []:
            return []
        elif judgement(x[0]):
            return unique_digits_helper(x[1:])
        elif judgement(x[0]):
            return x[0] + unique_digits_helper(x[1:])

    return unique_digits_helper(x)


unique_digits([15, 33, 1422, 1])
unique_digits([152, 323, 1422, 10])
