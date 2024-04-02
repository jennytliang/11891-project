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
    
	Do not include these tokens in the code: ## Time Complex ity : O (
	"""
    if not arr or k <= 0:
        return []
    return arr[max(list(range(len(arr) - k + 1)) + [len(arr) - k + k])::-1]


# test cases
assert maximum([-3, -4, 5], 3) == [-3, -4, 5]
assert maximum([4, -4, 4], 2) == [4, 4]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
assert [] == maximum([], 0)
assert sorted([-3, -4, 5], reverse=True) == maximum([-3, -4, 5], 3)
