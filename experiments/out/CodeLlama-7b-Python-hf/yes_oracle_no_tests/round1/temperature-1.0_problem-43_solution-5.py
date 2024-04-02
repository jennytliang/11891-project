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


def pairs_sum_to_x(l, x):
    """
    pairs_sum_to_x takes a list and an integer as input.
    it returns True if there are two distinct elements in the list that
    sum to the integer x, and False otherwise.
    >>> pairs_sum_to_x ([1, 3, -2, 1], 2)
    False
    >>> pairs_sum_to_x ([1, 3, -2, 1], 0)
    True
    >>> pairs_sum_to_x ([1, 3, -2, 1], 3)
    True
    >>> pairs_sum_to_x ([1, -2, 3, 4], 5)
    True
    >>> pairs_sum_to_x ([2, 4, -5, 3, 5, 7], 5)
    True
    """
