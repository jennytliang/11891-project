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
    
	Include these tokens in the code: all
	Do not include these tokens in the code: not arr : return [] if
	"""

  def pluck(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    if not arr:
        return []

    min_even_value = None
    min_even_value_index = None

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if not min_even_value:
                min_even_value = value
                min_even_value_index = index
            elif value < min_even_value:
                min_even_value = value
                min_even_value_index = index

    return [min_even_value, min_even_value_index] if min_even_value else []

if __name__ == '__main__':
    # Case 1
    print(pluck([4,2,3]))

    # Case 2
    print(pluck([1,2,3]))

    # Case 3
    print(pluck([]))

    # Case 4
    print(pluck([5, 0, 3, 0, 4, 2]))
    # Case 5
    print(pluck([1,2,3,4,5,6,7,8,9,10]))
    # Case 6
    print(pluck([2,4,6,8,10]))

    # Case 7
    print(pluck([1,2,3,4,5,6,7,8,9,10,11]))

    # Case 8
    print(pluck([1,2,3,4,5,6,7,8,9,10,11,12]))

    # Case 9
    print(pluck([1,2,3,4,5,6,7,8,9,10,11,12,13]))

    # Case 10
    print(pluck([1,2,3,4,5,6,7,8,9,10,11,12,13,14