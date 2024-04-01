def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: for ch in str
	Do not include these tokens in the code: return all
	"""


    def judge(x):
 
        if len(str(x)) == len(set(str(x))):
            return True
        else:
            return False

    return [x for x in x if judge(x)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
