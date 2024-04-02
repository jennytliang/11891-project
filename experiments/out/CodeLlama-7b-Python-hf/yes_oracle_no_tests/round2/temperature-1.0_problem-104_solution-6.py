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
    "takes list, returns list"
    unique_list = []
    for i in x:
      if i < 10:
        if i % 2 != 0:
          unique_list.append(i)
      
      else:
        a = i % 10
        b = i / 10
        if a % 2 is not 0:        
          unique_list.append(i)
          
        if b % 2 is not 0:
          unique_list.append(i)
       
    unique_list.sort()
    return unique_list
