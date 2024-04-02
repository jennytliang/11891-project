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


    foos = set()
    for i in range(len(l)):
        if (l[i] in foos):
            return True
        else:
            foos.add(-l[i])
    return False

def pairs_sum_to_zero_better(l):
    """
    pairs_sum_to_zero_better takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero_better([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero_better([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero_better([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero_better([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero_better([1])
    False
    
	Include these tokens in the code: range ( len ( l )):
	Do not include these tokens in the code: r :
	"""

    for r in range(len(l)):
        if(l[r] == 0):
            return True
    for r in range(len(l)):
        for rr in range(len(l)):
            if(l[r] + l[rr] == 0):
                return True
    return False








































































































































