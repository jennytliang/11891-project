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


def minimum_and_maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return an array 
    with the first k elements of the array sorted in ascending order, and the 
    last k elements sorted in descending order.

    Example 1:

        Input: arr = [4, -4, 5, 2, -3, 3], k = 3
        Output: [-4, 2, 4, 3, 5, -3]

    Example 2:

        Input: arr = [2, 4, 3, 1], k = 2
        Output: [1, 2, 3, 4]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    arr.sort()
    return arr[:k] + arr[::-1][:k]


def max_consecutive_ones(binary):
    """
    Given a binary array, find the maximum number of consecutive 1s in this array.

    Example 1:

        Input: [1,1,0,1,1,1]
        Output: 3

    Example 2:

        Input: [1,0,1,1,0,1]
        Output: 2

    Note:
        1. The input array will only contain 0 and 1.
        2. The length of input array is a positive integer and will not exceed 10,000
    """
    max_ones = 0
    current_ones = 0
    for bit in binary:
        if bit == 1:
            current_ones += 1
        else:
            max_ones = max(max_ones, current_ones)
            current_ones = 0
    return max(max