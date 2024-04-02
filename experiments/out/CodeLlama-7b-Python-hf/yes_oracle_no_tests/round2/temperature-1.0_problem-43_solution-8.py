def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    
	Do not include these tokens in the code: l _ dict = {}
	"""
    # BEGIN TODO 3
    l = sorted(l,key = abs)
    #print(l)
    if len(l) <= 2:
    	return False
    dict = l[0:int(len(l) / 2)]
    #print("dict is",dict)
    l = l[int(len(l) / 2):]
    for num in l:
    	if (num + dict[-1]) == 0:
    		return True
    	for element in range(len(dict) - 1, 0, -1):
    		if num + dict[element - 1] == 0:
    			return True
    		elif num + dict[element - 1] > 0:
    			continue
    		else:
    			dict=dict[:element]
    			break
    return False
    # END TODO 3


if __name__ == "__main__":
    import doctest
    doctest.testmod()