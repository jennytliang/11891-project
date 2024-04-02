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
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: max
	"""

    return so.topk(arr, k)


def minimum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the minimum k numbers in arr.

    Example 1:

        Input: arr = [4, 5, 2, 10, 18, 20], k = 3
        Output: [2, 4, 10]

    Example 2:

        Input: arr = [19, 5, 14, 3, 10, 20], k = 2
        Output: [3, 10]

    Example 3:

        Input: arr = [4, 5, 2, 10, 18, 20], k = 1
        Output: [4]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [0, 1000].
        3. 0 <= k <= len(arr)
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: min
	"""

    return so.topk(arr, -k)


def maximum_centered_ranges(arr, k):
    """
    Given an array arr of integers and a positive integer k, find the maximum 
    possible sum of ranges on the array that have exactly k numbers.

    A range is defined as two numbers with a distance of exactly 1 between them.

    Example 1:

        Input: arr = [1, 2, 3], k = 2
        Output: 4
        Explanation: The ranges are [1, 2] and [2, 3].
    
    Example 2:

        Input: arr = [1, 2, 10, 11, 6, 7, 5, 8], k = 3
        Output: 29
        Explanation: The ranges are [