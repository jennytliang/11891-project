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
    
	Include these tokens in the code:  def digits ( x : int )
	"""

    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Intuition:
        - Keep a running sum of the first k elements.
        - If the sum is > 99, return early.
        - Add k to the running sum.
        - If k is less than len(arr), repeat process with k+1.

    Edge Cases:
        - If k > len(arr), return 0.
        - If k <= 0, return 0.
        - If arr is empty, return 0.
    """

    if k > len(arr) or k <= 0:
        return 0

    sum_ = 0
    for i in range(k):
        if arr[i] > 99:
            return sum_
        sum_ += arr[i]

    return sum_


    # if k <= 0 or k > len(arr) or not arr:
    #     return 0

    # sum_ = 0
    # for i in range(k):
    #     if arr[i] > 99:
    #         return sum_
    #     sum_ += arr[i]

    # if k < len(arr):
    #     return sum_ + add_elements(arr[k:], k)

    # return sum_

    # if k <= 0 or k > len(arr) or not arr:
    #     return 0

    # sum_ = 0
    # for i in range(k):
    #     if arr[i] > 99:
    #         return sum_
    #     sum_ += arr[i]

    # if k < len(arr):
    #     return sum_ + add_elements(arr[k:], k)

    # return sum_
