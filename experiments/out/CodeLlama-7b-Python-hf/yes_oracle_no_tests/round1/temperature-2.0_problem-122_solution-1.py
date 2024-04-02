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
    # 1. BASE CASE
    # if we have less than 2 digits, then the answer is the sum of the array
    if len(arr) <= 2:
        return sum(arr)
    # 2. RECURSIVE CASE
    # if we have 2 digits, then we need to check if the first 2 elements are valid
    # if they are valid, then we need to add the first 2 elements to the answer
    # if they are not valid, then we need to add the first element to the answer
    # otherwise, we need to add nothing to the answer
    # return the answer to the recursive case
    else:
        if digits(arr[0]) + digits(arr[1]) <= 2:
            return add_elements(arr[2:], k) + arr[0] + arr[1]
        else:
            return add_elements(arr[1:], k) + arr[0]


def digits(x):
    """
    Return the number of digits in a number
    """
    if x < 0:
        x = -x
    if x == 0:
        return 1
    return int(math.log10(x)) + 1


print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
