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
    
	Include these tokens in the code: range ( len ( l )):
	Do not include these tokens in the code: r :
	"""


    fo = 0
    for r in range(len(l)):
        for r1 in range(len(l)):
            if r1 != r and l[r] + l[r1] == 0:
                fo = 1
                break
        if fo == 1:
            break
    if fo == 1:
        return True
    else:
        return False
