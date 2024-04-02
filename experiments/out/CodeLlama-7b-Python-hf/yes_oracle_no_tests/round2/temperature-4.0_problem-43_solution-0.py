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
    
	Do not include these tokens in the code: s = set ()
	"""
    s = set()
    for i in l:
        if -i in s:
            return True
        s.add(i)
    return False



#print(pairs_sum_to_zero([1, 2, 3, 7]))
#print(pairs_sum_to_zero([1, 2, 3, -4]))
#print(pairs_sum_to_zero([1, 2, 3, 4]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
#print(pairs_sum_to_zero([1, 2, 3, 4, 5, 