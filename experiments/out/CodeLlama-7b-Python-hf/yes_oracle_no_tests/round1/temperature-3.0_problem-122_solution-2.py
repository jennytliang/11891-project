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
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: s = 0 for
	"""
    #############
    # Base cases
    #############
    if len(arr) <= k:
        return sum(arr)

    #############
    # Main code
    #############
    # Use a sliding window of size k
    # i: index of left-most element of the window
    # j: index of right-most element of the window
    # sum_arr: sum of elements in the window
    i, j, sum_arr = 0, 0, 0
    while j < len(arr):
        # Add the next element
        sum_arr += arr[j]
        # If there are more than 2 digits, remove the left-most element
        if digits(arr[i]) > 2:
            sum_arr -= arr[i]
            i += 1
        # Move the window one element to the right
        j += 1
    return sum_arr


def digits(n):
    """
    Return the number of digits in the integer n
    """
    if n == 0:
        return 1
    return int(math.log10(n)) + 1
