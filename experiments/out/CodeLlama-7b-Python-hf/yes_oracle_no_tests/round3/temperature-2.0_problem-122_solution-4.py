def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    pass


def find_max_subarray(arr):
    """
    Given an integer array arr, find a contiguous non-empty subarray
    with maximum sum.

    Example:

        Input: arr = [3, -1, 4, 1]
        Output: 6
        Explanation: arr[1] = -1, arr[2] = 4, so return max(3, -1 + 4, 4) = 6.

    Constraints:
        1. 1 <= arr.length <= 3 * 10^4
        2. -10^5 <= arr[i] <= 10^5

    Include these tokens in the code: def max_subarray ( arr : list ) -> int :
    """
    pass


def find_max_subarray_with_sum(arr, sum_):
    """
    Given an integer array arr, find a contiguous non-empty subarray
    with sum equal to sum. If there are multiple answers, return the
    subarray with minimum average.

    Example:

        Input: arr = [1, 2, 3, 4, 5], sum = 9
        Output: [2, 3, 4]

    Constraints:
        1. 1 <= arr.length <= 10^3
        2. -10^3 <= arr[i] <= 10^3
        3. sum <= 10^3

    Include these tokens in the code: def max_subarray_with_sum ( arr : list, sum : int ) -> list :
    """
    pass


def find_min_max(arr):
    """
    Given an integer array arr, find the minimum and maximum elements.
    You may assume none of the elements are repeated.

    Example:

        Input: arr = [2, 3, 4, 5, 1]
        Output: [1, 5]

    Constraints:
        1. 1 <= arr.length <= 5 * 10^4
        2. -