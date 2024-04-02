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
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr[0], 0]

    # find the smallest even number
    smallest_even = None
    smallest_even_index = None
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if smallest_even is None or val < smallest_even:
                smallest_even = val
                smallest_even_index = i

    if smallest_even is None:
        return []

    # find the smallest index of the smallest even number
    smallest_even_index_min = None
    for i, val in enumerate(arr):
        if val == smallest_even:
            if smallest_even_index_min is None or i < smallest_even_index_min:
                smallest_even_index_min = i

    return [smallest_even, smallest_even_index_min]


if __name__ == "__main__":
    # Test Case 1
    print(pluck([4, 2, 3]))
    # Test Case 2
    print(pluck([1, 2, 3]))
    # Test Case 3
    print(pluck([]))
    # Test Case 4
    print(pluck([5, 0, 3, 0, 4, 2]))
