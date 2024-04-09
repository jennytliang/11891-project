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
	Do not include these tokens in the code: d
	"""



    # add your code here
    count = 0
    for i in range(k):
        if len(str(arr[i])) == 1:
            count += arr[i]
        elif len(str(arr[i])) == 2:
            count += arr[i]
    return count
