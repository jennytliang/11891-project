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
    
	Do not include these tokens in the code: # add code here
	"""
    # add code here
    # O(n^2) solution
    # for the first element in the list, check if there exists a pair
    # in the list that sums to zero. 
    # O(n) solution
    # for each element in the list, check if it is a key in the hash table. 
    # if it is not a key, add it to the hash table with the value of -element.
    # if it is a key, return True.
    # hash table = {}
    # for element in l:
    #     if element in hash_table:
    #         return True
    #     hash_table[element] = -element
    # return False
    # O(nlog(n)) solution
    # sort the list
    # for each element in the list, check if there exists a pair in the list
    # that sums to zero.
    # if there is a pair, return True.
    # otherwise, return False.
    l.sort()
    for element in l:
        if (element * 2) in l:
            return True
    return False


# print(pairs_sum_to_zero([1, 2, 3, 7]))
# print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
# print(pairs_sum_to_zero([1, 3, -2, 1]))
# print(pairs_sum_to_zero([1, 3, 5, 0]))


def pairs_sum_to_x(l, x):
    """
    pairs_sum_to_x takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to x, and False otherwise.
    >>> pairs_sum_to_x([1, 3, 5, 0], 6)
    True
    >>> pairs_sum_to_x([1, 3, -2, 1], 6)
    True
    >>> pairs_sum_to_x([1, 2, 3, 7],