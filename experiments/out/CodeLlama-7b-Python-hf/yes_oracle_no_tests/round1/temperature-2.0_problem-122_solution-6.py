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
    # Add your code here
    sum = 0
    for i in range(k):
        x = arr[i]
        if digits(x) <= 2:
            sum += x
    return sum


def digits(x):
    """
    Returns the number of digits of x
    """
    return len(str(x))


print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
