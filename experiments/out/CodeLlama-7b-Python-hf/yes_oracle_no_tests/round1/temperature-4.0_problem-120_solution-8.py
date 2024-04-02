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
    
	Include these tokens in the code: return sorted ( sorted ( arr )[ :: - 1
	"""
    return sorted(sorted(arr)[::-1])[:k]


def minimum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the minimum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

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
    """
    return sorted(sorted(arr))[:k]


def maximum_of_subarrays(arr, k, n):
    """
    Given an array arr of integers and a positive integer k, find the maximum 
    values of each of the contiguous subarrays of length k in the array. The 
    answer is an array of length n - k + 1 where answer[i] is the maximum value 
    of a subarray of length k which starts at index i in the original array.

    Example 1:

        Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        Output: [3, 3, 5, 5, 6, 7]

    Example 2:

        Input: arr = [1, 5, 1, 5, 5, 5, 1, 1, 1], k = 4
        Output: [5, 5, 5, 5]

    Note