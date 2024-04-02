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
	Do not include these tokens in the code: pass import numpy as np
	"""
    # -----------------------------------------------------------------------------
    # YOUR CODE STARTS
    # Check the code to see the number of times import is used.
	
	judge_list = []

	for item in x:
		item_str = str(item)
		for number in item_str:
			if "2" in number or \
			 "4" in number or \
			 "6" in number or \
			 "8" in number:
				break
			elif number == item_str[-1]:
				judge_list.append(item)
				
	return judge_list
    # YOUR CODE ENDS
    # -----------------------------------------------------------------------------
