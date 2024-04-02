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
    """
    Time Complexity: O(k)
    Space Complexity: O(1)
    """
    # sum of the first k elements
    sum_k = 0
    # count of the first k elements
    count_k = 0

    # iterate through the array
    for i in range(len(arr)):
        # if the count of the first k elements is less than k
        if count_k < k:
            # if the element is less than 100
            if arr[i] < 100:
                # sum the element
                sum_k += arr[i]
                # increment the count of the first k elements
                count_k += 1
        # if the count of the first k elements is equal to k
        elif count_k == k:
            # return the sum of the first k elements
            return sum_k


def add_elements_array(arr, k):
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
    """
    Time Complexity: O(k)
    Space Complexity: O(1)
    """
    # sum of the first k elements
    sum_k = 0
    # count of the first k elements
    count_k = 0

    # iterate through the array
    for i in range(len(arr)):
        # if the count of the first k elements is less than k
        if count_k < k:
            # if the element is less than 100
            if arr[i] <