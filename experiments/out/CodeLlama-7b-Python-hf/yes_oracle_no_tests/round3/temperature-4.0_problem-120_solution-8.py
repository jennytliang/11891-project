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
    
	Include these tokens in the code: )[ :: - 1 ][ :
	Do not include these tokens in the code: ) [:
	"""


    return sorted(sort_by_value(arr), reverse=True)[:k]

def sort_by_value(arr):
    """
    Return a list of (value, index) tuples sorted by the value in descending order.

    Example 1:

        Input: arr = [-3, -4, 5]
        Output: [(5, 2), (-4, 1), (-3, 0)]

    Example 2:

        Input: arr = [4, -4, 4]
        Output: [(4, 0), (4, 2), (-4, 1)]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1]
        Output: [(2, 1), (2, 3), (1, 2), (1, 7), (-2, 5), (-1, 4), (-3, 0)]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
    """

    return sorted(enumerate(arr), key=lambda x: x[1], reverse=True)
