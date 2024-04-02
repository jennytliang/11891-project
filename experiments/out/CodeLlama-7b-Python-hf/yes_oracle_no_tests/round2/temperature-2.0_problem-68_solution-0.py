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
    # Find the smallest even value
    # Find the smallest index
    # Return the smallest even value with the smallest index
    # Return [] if there is no even value
    # Return [] if the array is empty
    # O(n) time | O(1) space - where n is the length of the input array
    # if not arr:
    #     return []

    # smallest_even = min([n % 2 for n in arr if n % 2 == 0])
    # smallest_index = None
    # for i, val in enumerate(arr):
    #     if val % 2 == smallest_even:
    #         if smallest_index is None or i < smallest_index:
    #             smallest_index = i
    # return [smallest_even, smallest_index] if smallest_even is not None else []

    smallest_even = None
    smallest_index = None
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if smallest_even is None or val < smallest_even:
                smallest_even = val
                smallest_index = i
    return [smallest_even, smallest_index] if smallest_even is not None else []

if __name__ == "__main__":
    # Test Case 1
    input1 = [4,2,3]
    output1 = [2, 1]
    actual1 = pluck(input1)
    print("Test case 1")
    print("Actual:", actual1)
    print("Expected:", output1)

    # Test Case 2
    input2 = [1,2,3]
    output2 = [2, 1]
    actual2 = pluck(input2)
    print("Test case 2")
    print("Actual:", actual2)
    print("Expected:", output2)

    # Test Case 3
    input3 = []
    output3 = []
    actual3 = pluck(input3)
    print("Test case 3")
    print("Actual:", actual3)
    print("Expected:", output3