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
    # Find the smallest even number
    # If there is no even number, return []
    # If there is an even number, find the smallest number
    # Return the smallest number and its index
    if not arr:
        return []

    # Find the smallest even number
    smallest_even = float("inf")
    smallest_even_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even:
            smallest_even = arr[i]
            smallest_even_index = i

    if smallest_even == float("inf"):
        return []

    # Find the smallest number
    smallest_index = -1
    smallest_number = float("inf")
    for i in range(len(arr)):
        if arr[i] < smallest_number:
            smallest_number = arr[i]
            smallest_index = i

    return [smallest_number, smallest_index]


def pluck_test():
    # assert pluck([]) == []
    # assert pluck([1, 3, 5]) == []
    # assert pluck([4, 2, 3]) == [2, 1]
    # assert pluck([1, 2, 3]) == [2, 1]
    # assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([2, 3, 4, 5, 6]) == [2, 0]
    assert pluck([2, 3, 4, 5, 6, 7]) == [2, 0]
    assert pluck([2, 3, 4, 5, 6, 7, 8]) == [2, 0]
    assert pluck([2, 3, 4, 5, 6, 7, 8, 9]) == [2, 0]
    assert pluck([2, 3, 4, 5, 6, 7, 8, 9, 1