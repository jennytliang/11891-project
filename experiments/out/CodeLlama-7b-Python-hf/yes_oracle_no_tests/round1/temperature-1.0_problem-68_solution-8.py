def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    
	Include these tokens in the code: if all ( val %
	"""
    
    # the first non-zero value is the smallest even number (small_even)
    # the index of the first non-zero value is smaller than any other even number (small_even_idx)
    # if not - return empty list
    # return

    # find the smallest even number in array. save it as a variable to compare to other non-zero numbers
    # save the smallest index of that number.
    # iterate through all numbers in array to find index of the small_even value.
    # after you find that number, return that val and its index.
    # If you can't find any non-zero numbers, return
    
    small_even = 400 # just set a big number.
    small_even_idx = -1
    
    for c, val in enumerate(arr):
        # c is an index,
        # val is a value,
        # the for loop will iterate c through each value in the array
        # if value is not zero
        if val != 0 and val % 2 == 0: # can't mod by 0
        # if value is not zero and is divisible by 2
            # find smallest even val and save it to small_even variable
            if val < small_even:
                small_even = val
                small_even_idx = c
            # else, continue
            continue
    ## now find the idx of the smallest even number within a list of numbers divisible by 2   
    
    smallest_index = -1
        
    for index, item in enumerate(arr):
        # if you're comparing a list to itself
            # start index from 1, and keep comparing numbers
            # if small_even == item,
                # save the index of the smallest_even val as smallest_index
                # return [small_even, smallest_index]
    # if this doesn't work, try the following...
        # for index, item in enumerate(arr):
        # if val % 2 == 0:
        # if item == small_even:
        # smallest_index = item
        # return
    # if this doesn't work, try the following...
