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

    # add code here
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == 0:
                return True
    return False


# print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
# print(pairs_sum_to_zero([1, 2, 3, 7]))
# print(pairs_sum_to_zero([1, 3, -2, 1]))
# print(pairs_sum_to_zero([1, 3, 5, 0]))
# print(pairs_sum_to_zero([1]))


def pairs_sum_to_x(l, x):
    """
    pairs_sum_to_x takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to x, and False otherwise.
    >>> pairs_sum_to_x([1, 3, 5, 0], 4)
    False
    >>> pairs_sum_to_x([1, 3, -2, 1], 5)
    True
    >>> pairs_sum_to_x([1, 2, 3, 7], 4)
    False
    >>> pairs_sum_to_x([2, 4, -5, 3, 5, 7], 9)
    True
    >>> pairs_sum_to_x([1], 4)
    False
    
	Include these tokens in the code: for i in range ( len ( l )):
	"""

    # add code here
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == x:
                return True
    return False


# print(pairs_sum_to_x([2, 4, -5, 3, 5, 7], 9))
# print(pairs_sum_to