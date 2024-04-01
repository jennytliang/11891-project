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
    """
    min_node_val, min_node_index = arr[0], 0
    for node in arr[1:]:
        if node % 2 == 0:
            if node < min_node_val:
                min_node_val = node
                min_node_index = arr.index(node)
        elif min_node_val % 2 == 0 and node % 2 != 0:
            # if there is a node which has an odd value as the minimum value, then it is better than the min node
            min_node_val = node
            min_node_index = arr.index(node)
        elif min_node_val % 2 != 0 and node % 2 != 0:
            if node < min_node_val:
                min_node_val = node
                min_node_index = arr.index(node)
        else:
            if node < min_node_val:
                min_node_val = node
                min_node_index = arr.index(node)
    return [min_node_val, min_node_index]


if __name__ == "__main__":
    assert pluck([1, 2, 3]) == [2, 1]
