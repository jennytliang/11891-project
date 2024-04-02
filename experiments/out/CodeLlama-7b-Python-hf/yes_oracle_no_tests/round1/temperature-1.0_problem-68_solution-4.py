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

    min_value = min(arr)
    min_value_index = arr.index(min_value)

    min_even_value = min_value
    min_even_value_index = min_value_index

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if value < min_even_value:
                min_even_value = value
                min_even_value_index = index
            elif value == min_even_value and index < min_even_value_index:
                min_even_value_index = index

    if min_even_value == min_value:
        return [min_even_value, min_even_value_index]
    else:
        return [min_even_value, min_even_value_index]


if __name__ == "__main__":
    arr = [5, 0, 3, 0, 4, 2]
    assert pluck(arr) == [0, 1]

    arr = [4, 2, 3]
    assert pluck(arr) == [2, 1]

    arr = [1, 2, 3]
    assert pluck(arr) == [2, 1]

    arr = []
    assert pluck(arr) == []
