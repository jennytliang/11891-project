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

    if arr:
        even_values = [el for el in arr if el%2 == 0]
        if even_values:
            even_values.sort()
            if len(even_values) == 1:
                return [even_values[0], arr.index(even_values[0])]
            even_values_even_indices = []

            for idx, val in enumerate(even_values):
                if val in arr and arr.index(val) % 2 == 0 and idx == 0:
                    even_values_even_indices.append(idx)
                if val in arr and arr.index(val) % 2 == 0 and idx > 0:
                    pre_val, pre_idx = even_values_even_indices[idx-1]
                    print(pre_idx, pre_val)
                    if pre_val >= val:
                        even_values_even_indices.append(idx)

            if even_values_even_indices:
                even_values_even_indices.sort(key = lambda n : arr.index(n))
                val, idx = even_values_even_indices[0]
                return [val, arr.index(val)]
        return [arr[0], 0]
    return []