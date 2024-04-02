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
    # [ 4,2,3 ]
    # 4, 2, 3
    # 2, 0, 1

    smallest_value = 99999
    smallest_index = -1

    for index, val in enumerate(arr):
        if (
            val % 2 == 0 and
            val <= smallest_value
        ):
            smallest_index = index
    
    return [smallest_index, smallest_index]

def pluck_recursive(arr):
    """
    Solution with recursion
    """
    smallest_value = 9999
    smallest_index = -1

    def helper(smallest_value, smallest_index, arr):

        if not arr:
            return

        if arr[0] % 2 == 0 and arr[0] < smallest_value:
            smallest_value = arr[0]
            smallest_index = 0
        
        helper(smallest_value, smallest_index, arr[1:])

    helper(smallest_value, smallest_index, arr)

    return [smallest_index, smallest_index]

print(pluck([4,2,3])) # [1,0]
print(pluck([1,2,3])) # [1,0]
print(pluck([1,3,4,2])) # [0,1]
print(pluck([3])) # []
print(pluck([1,3,4,6])) # []
print(pluck([9,10,11,12])) # [0,1,2,3]
print(pluck([5,0,3,0,4,2])) # [2,3]
print(pluck([2])) # []
print(pluck([1])) # []
print(pluck([4,3,4,6])) # [1,2]
print(pluck([4,5,5,4])) # [1,0]
print(pluck([8])) # []
print(pluck([20, 1])) # [0,0]
