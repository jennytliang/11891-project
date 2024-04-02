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
	"""
    import re
    L1 = list(filter(lambda num: len(set(str(num))) == len(str(num)),[x for x in range(1,100000) if x%2]))
    return L1.sort()
   
    return [x for x in range(1,100000) if x%2]

print(unique_digits(1422))
print([x for x in range(1,100000) if x%2 !=0])
