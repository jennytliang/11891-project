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
    
	Include these tokens in the code: for i in range ( len ( l )):
	"""
    l_dict = {}
    for i in range(len(l)):
        l_dict[l[i]] = l[i]
    for i in range(len(l_dict)):
        if l_dict[l[i]] + l[i] == 0:
            return True
    return False

print(pairs_sum_to_zero([1, 3, 5, 0]))
print(pairs_sum_to_zero([1, 3, -2, 1]))
print(pairs_sum_to_zero([1, 2, 3, 7]))
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
print(pairs_sum_to_zero([1]))