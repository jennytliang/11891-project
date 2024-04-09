def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: a = [] for i
	"""
    def judge(x):
        for i in str(x):
            if '2' <= i <= '9' and int(i) % 2 == 0:
                return False
            elif '0' <= i <= '9' and int(i) % 2 != 0:
                return True
        return True

    return sorted([x for x in x if judge(x)])


print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))

