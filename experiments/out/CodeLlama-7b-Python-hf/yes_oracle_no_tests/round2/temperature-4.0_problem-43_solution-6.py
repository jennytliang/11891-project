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
    # write your code here
    # 1. create a list of all possible pairs in the input list
    # 2. check if any of those pairs sums to zero
    # 3. return True if any of them does, and False otherwise
    # hint: use the sum() function to find the sum of a list
    # hint: use the in operator to check if an item is in a list
    # hint: use the second parameter of range to count from the end
    # hint: use enumerate to get the index of the current element
    # hint: use the break statement to exit a loop early
    pass
