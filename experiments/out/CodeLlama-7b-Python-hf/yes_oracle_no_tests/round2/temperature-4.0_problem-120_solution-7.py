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
    
	Include these tokens in the code: sorted (
	"""

    return so.maximum(arr, k)


def minimum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the minimum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-3, -4, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [-4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [-3]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Include these tokens in the code: sorted (
	"""

    return so.minimum(arr, k)


def maximum_subarray_sum(arr, k):
    """
    Given an array arr of integers and a positive integer k, find the maximum 
    subarray sum of k consecutive elements in the array.

    Example 1:

        Input: arr = [1, 1, 1, 1, 1], k = 2
        Output: 2

    Example 2:

        Input: arr = [1, 2, 1, 2, 1, 2, 1], k = 2
        Output: 5

    Example 3:

        Input: arr = [-1, -2, -2, -1], k = 2
        Output: 0

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].