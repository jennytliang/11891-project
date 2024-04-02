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
    
	Include these tokens in the code: def digits ( x : int ) -> int
	Do not include these tokens in the code: # Sum of the first k elements
	"""
    summ = 0
    num_dig_arr = [list(map(int, str(num))) for num in arr]
    num_len_arr = [len(num) for num in num_dig_arr]
    for ii in range(len(num_len_arr)):
        if num_len_arr[ii] <= 2 and ii < k:
            for jj in range(num_len_arr[ii]):
                summ += num_dig_arr[ii][jj]
    return summ
