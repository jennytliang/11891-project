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
	Do not include these tokens in the code: result = [] for i
	"""
    digits_set = {}
    unique_list = []

    def has_even_digit(x):
        """Given a single int x > 0. return true if there's any even digit in x.
        >>> has_even_digit(145929)
        True
        >>> has_even_digit(73779)
        False"""
        digits = set()
        while x:
            digits.add(x % 10)
            x = x // 10
        res = False 
        for i in digits:
            if i % 2 == 0:
                res = True

        return res 

    for item in x:
        if has_even_digit(item) == False:
            unique_list.append(item)
            unique_list.sort()

    return unique_list

print(unique_digits([15, 33, 1422, 1]))