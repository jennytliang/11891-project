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
    
	Do not include these tokens in the code: # your code here
	"""

    # write your code here
    if len(l) < 2:
        return False
    l.sort()
    for i in range(len(l)-1):
        if l[i] + l[-1] == 0:
            return True
        elif l[i] + l[i+1] == 0:
            return True
    return False

print(pairs_sum_to_zero([1, 2, 3, 7]))


