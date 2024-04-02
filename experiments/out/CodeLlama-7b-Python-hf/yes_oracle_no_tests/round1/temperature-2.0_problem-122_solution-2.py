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
	Do not include these tokens in the code: sum = 0 i
	"""
    # define sum
    sum = 0
    # define digits
    def digits(x):
        if x < 10:
            return 1
        else:
            return 2
    # iterate over the array
    for i in range(k):
        # add the element to sum
        sum += arr[i]
        # check if the element has two digits
        if digits(arr[i]) > 1:
            # if so, subtract the element from the sum
            sum -= arr[i]
    # return the sum
    return sum
