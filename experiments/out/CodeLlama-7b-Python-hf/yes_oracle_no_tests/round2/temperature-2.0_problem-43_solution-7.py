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
	Do not include these tokens in the code: r n ge
	"""


    fo = set(l)
    for x in fo:
        if (x == 0) or (x * 2 in fo):
            return True
    return False




if __name__ == "__main__":
    import doctest
    doctest.testmod()
