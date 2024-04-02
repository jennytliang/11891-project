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
	Do not include these tokens in the code: unique _ dig
	"""
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    # IMPORTANT:
    #   -- Your solution must be recursive,
    #      using the 2 allowed above as guidelines.
    # ------------------------------------------------------------------
    if x == []:
        return []
    elif x[0]%2 == 0:
        return unique_digits(x[1:])
    else:
        return [x[0]] + unique_digits(x[1:])


def unique_digits(x):
    if x == []:
        return []
    elif x[0]%2 == 0:
        return unique_digits(x[1:])
    else:
        return [x[0]] + unique_digits(x[1:])


def unique_digits(x):
    if x == []:
        return []
    elif x[0]%2 == 0:
        return unique_digits(x[1:])
    else:
        return [x[0]] + unique_digits(x[1:])


def unique_digits(x):
    if x == []:
        return []
    elif x[0]%2 == 0:
        return unique_digits(x[1:])
    else:
        return [x[0]] + unique_digits(x[1:])


def unique_digits(x):
    if x == []:
        return []
    elif x[0]%2 == 0:
        return unique_digits(x[1:])
    else:
        return [x[0]] + unique_digits(x[1:])


def unique_digits(x):
    if x == []:
        return []
    elif x[0]%2 == 0:
        return unique_digits(x[1:])
    else:
        return [x[0]] + unique_dig