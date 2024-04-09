def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: i
	"""

    def judge(x):
       if x%2==0:
          return False
       else:
          return True
    return sorted(list(filter(judge,x)))

def unique_digits_2(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: i
	"""
    return sorted(list(filter(lambda x:not x%2,x)))

if __name__=="__main__":
    import doctest
    doctest.testmod()