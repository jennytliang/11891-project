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
    
	Include these tokens in the code: : int ) -> int : s =
	Do not include these tokens in the code: ):
	"""


    def di_sum(arr, k):
        s = 0
        for i in range(k):
            s += arr[i]
        return s

    def add_elements_helper(arr, k):
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        else:
            return arr[0] + add_elements_helper(arr[1:], k)

    return add_elements_helper(arr, k)












