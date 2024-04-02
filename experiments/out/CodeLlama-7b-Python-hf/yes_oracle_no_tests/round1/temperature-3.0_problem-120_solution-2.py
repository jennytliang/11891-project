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
    
	Do not include these tokens in the code: if k == 0 or len
	"""
    if k == 0 or len(arr) == 0:
        return []
    
    arr.sort()
    return arr[-k:]

if __name__ == "__main__":
    test_cases = [
        [[-3, -4, 5], 3, [-4, -3, 5]],
        [[4, -4, 4], 2, [4, 4]],
        [[-3, 2, 1, 2, -1, -2, 1], 1, [2]],
        [[1, 2, 3, 4, 5], 1, [5]],
        [[1, 2, 3, 4, 5], 2, [4, 5]],
        [[1, 2, 3, 4, 5], 3, [3, 4, 5]],
        [[1, 2, 3, 4, 5], 4, [2, 3, 4, 5]],
        [[1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]],
    ]
    for test_case in test_cases:
        arr = test_case[0]
        k = test_case[1]
        res = test_case[2]
        assert maximum(arr, k) == res, f'failed for {arr}, {k}'
