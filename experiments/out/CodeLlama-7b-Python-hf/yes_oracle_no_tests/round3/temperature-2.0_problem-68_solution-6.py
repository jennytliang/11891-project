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

    # # Version 1 - Naive
    # def pluck(arr):
    #     # # Check that the array is not empty
    #     if not arr:
    #         return []

    #     # # Check that all values are non-negative
    #     if any(x < 0 for x in arr):
    #         return []

    #     # # Check that all values are even
    #     if any(x % 2 != 0 for x in arr):
    #         return []

    #     # # Get the smallest value
    #     smallest = min(arr)

    #     # # Get the smallest index
    #     smallest_index = arr.index(smallest)

    #     return [smallest, smallest_index]

    # # Version 2 - Using min
    # def pluck(arr):
    #     # Check that the array is not empty
    #     if not arr:
    #         return []

    #     # # Check that all values are non-negative
    #     if any(x < 0 for x in arr):
    #         return []

    #     # # Check that all values are even
    #     if any(x % 2 != 0 for x in arr):
    #         return []

    #     # Get the smallest value
    #     smallest = min(arr)

    #     # Get the smallest index
    #     smallest_index = arr.index(smallest)

    #     return [smallest, smallest_index]

    # Version 3 - Using min and enumerate
    def pluck(arr):
        # Check that the array is not empty
        if not arr:
            return []

        # # Check that all values are non-negative
        if any(x < 0 for x in arr):
            return []

        # # Check that all values are even
        if any(x % 2 != 0 for x in arr):
            return []

        # Get the smallest value and its index
        smallest, smallest_index = min((x, i) for i, x in enumerate(arr) if