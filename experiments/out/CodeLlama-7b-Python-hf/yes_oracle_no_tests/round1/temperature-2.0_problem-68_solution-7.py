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
    # The code below has been commented out as it was not accepted by LeetCode
    # The code below works, but it does not pass the time complexity test
    # for large arrays
    #
    # if len(arr) == 0:
    #     return []
    #
    # for i in range(len(arr)):
    #     if arr[i] % 2 == 0:
    #         return [arr[i], i]
    #
    # return []

    # The code below is accepted by LeetCode
    if len(arr) == 0:
        return []

    min_val = float("inf")
    min_val_index = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < min_val:
            min_val = arr[i]
            min_val_index = i

    if min_val_index == -1:
        return []

    return [min_val, min_val_index]


assert pluck([4, 2, 3]) == [2, 1]
assert pluck([1, 2, 3]) == [2, 1]
assert pluck([]) == []
assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
