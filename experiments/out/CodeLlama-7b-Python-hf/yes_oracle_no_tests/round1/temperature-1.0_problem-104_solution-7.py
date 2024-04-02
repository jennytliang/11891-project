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
    digits_set = '123456789'
    for _ in range(len(x)):
        number = str(x[_])
        for j in number:
            if j in digits_set:
                break
            else:
                digits_set = digits_set.replace(j,'')
                if len(digits_set) <= 1:
                    return []                    
        
    x = sorted(set(x))
    return sorted([i for i in x if i%2 != 0])
    
print (unique_digits([15, 33, 1422, 1]))
print (unique_digits([152, 323, 1422, 10]))
