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

    def two_digits_sum(x):
        if x < 10:
            return x

        return x % 10 + x // 10

    # add elements with two digits
    result = 0
    for i in range(min(len(arr), k)):
        result += two_digits_sum(arr[i])

    # add elements without two digits
    for i in range(k, len(arr)):
        result += arr[i]

    return result


print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
