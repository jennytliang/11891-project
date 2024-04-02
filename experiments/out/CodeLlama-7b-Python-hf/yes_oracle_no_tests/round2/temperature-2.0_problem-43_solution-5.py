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
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r _
	"""


    foobar = []
    for i in l:
        for j in l:
            if i == j or i in foobar or j in foobar:
                continue
            if i + j == 0:
                return True
            foobar.append(i)
            foobar.append(j)
    return False


print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
