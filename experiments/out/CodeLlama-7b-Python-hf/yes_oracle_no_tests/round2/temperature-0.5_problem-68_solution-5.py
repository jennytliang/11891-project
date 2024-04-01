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
    # initialize smallest even value
    smalest_val = float("inf")
    # initialize smallest even value index
    smalest_index = float("inf")
    # initialize the smallest even value found
    smallest_even_val = float("inf")
    # initialize the smallest even value found index
    smallest_even_index = float("inf")
    # iterate through array
    for index, val in enumerate(arr):
        # check if val is even
        if val % 2 == 0:
            # check if val is smaller than smallest even value
            if val < smalest_val:
                # set smalest even value to val
                smalest_val = val
                # set smalest even index to index
                smalest_index = index
            # check if val is even and smaller than smallest even value
            elif val == smalest_val:
                # check if index is smaller than smallest even index
                if index < smalest_index:
                    # set smalest even index to index
                    smalest_index = index
    # check if smalest even value is smaller than smallest even value
    if smalest_val < smallest_even_val:
        # set smallest even value to smalest even value
        smallest_even_val = smalest_val
        # set smallest even index to smalest even index
        smallest_even_index = smalest_index
    # check if smalest even value is equal to smallest even value
    elif smalest_val == smallest_even_val:
        # check if smalest even index is smaller than smallest even index
        if smalest_index < smallest_even_index:
            # set smallest even index to smalest even index
            smallest_even_index = smalest_index
    # return smallest even value and index
    return [smallest_even_val, smallest_even_index] if smallest_even_val != float(
        "inf"
    ) else []
