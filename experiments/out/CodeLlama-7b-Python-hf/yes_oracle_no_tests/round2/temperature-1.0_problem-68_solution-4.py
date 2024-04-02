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
    # Setup
    if arr == []:
        return []
    # Solution
    # 1. Find the index of the smallest even value
    # 2. Find the index of the smallest even value that has the same index
    # 3. Return the index and the value
    # 4. If no even values, return []
    # 5. If no even values, return []
    # 6. If no even values, return []
    # 7. If no even values, return []
    # 8. If no even values, return []
    # 9. If no even values, return []
    # 10. If no even values, return []
    # 11. If no even values, return []
    # 12. If no even values, return []


print(pluck([1, 2, 3]))
print(pluck([4, 2, 3]))
print(pluck([1, 2, 3, 4]))
print(pluck([1, 2, 3, 4, 5]))
print(pluck([5, 0, 3, 0, 4, 2]))
