def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ): for ch in
	"""
    unique = []
    for i in x:
        if is_unique(i):
            unique.append(i)
    return sorted(unique)

def is_unique(x):
    """Checks if the given number has any even digits.
    
    For example:
    >>> is_unique(152)
    False
    >>> is_unique(15)
    True
    """
    for ch in str(x):
        if int(ch) % 2 == 0:
            return False
    return True
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()