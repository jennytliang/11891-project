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
	Do not include these tokens in the code: r n age
	"""


    for i in range(len(l)):
        fo0=-l[i]
        for j in range(i):
            if(l[j]==fo0):
                return True
    return False
         
def sum_to_five(l):
    """
    sum_to_five takes a list of integers as an input.
    it returns True if there are an odd number of distinct integers,
    and False otherweise.
    >>> sum_to_five([10, 1, 5, 2, 7, 9, 3, 4])
    False
    >>> sum_to_five([4, 8, 3, 8, 2]) # odd
    True
    >>> sum_to_five([]) # empty list is False
    False
    >>> sum_to_five([1]) # length 1 is True
    True
    
	Use sum() and range().
    """
