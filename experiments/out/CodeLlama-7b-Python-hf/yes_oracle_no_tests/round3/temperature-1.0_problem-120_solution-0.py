def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Include these tokens in the code: return sorted
	Do not include these tokens in the code: # Get the list of top k
	"""
    return sorted(arr, reverse=True)[:k]


if __name__ == "__main__":
    # Test Case 1
    input1 = [-3, -4, 5]
    input2 = 3
    expected = [-4, -3, 5]
    result = maximum(input1, input2)
    print("Test 1")
    print("Expected:", expected)
    print("Result:", result)

    # Test Case 2
    input1 = [4, -4, 4]
    input2 = 2
    expected = [4, 4]
    result = maximum(input1, input2)
    print("Test 2")
    print("Expected:", expected)
    print("Result:", result)

    # Test Case 3
    input1 = [-3, 2, 1, 2, -1, -2, 1]
    input2 = 1
    expected = [2]
    result = maximum(input1, input2)
    print("Test 3")
    print("Expected:", expected)
    print("Result:", result)
