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
    
	Include these tokens in the code: digits
	Do not include these tokens in the code: two _ dig its _ sum
	"""


  # Add your code here
    i = 0
    j = k
    arr_sum = 0
    while j < len(arr):
        str_arr = str(arr[i])
        if len(str_arr) == 1:
            arr_sum += arr[i]
        elif len(str_arr) == 2:
            arr_sum += arr[i]
        i += 1
        j += 1
    return arr_sum






































































































































































































































































































































































































