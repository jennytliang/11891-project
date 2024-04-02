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
    # first find the number of digits in the first k elements
    digits = 0
    for i in range(k):
        n = len(str(arr[i]))
        digits += n

    # now add the elements with the appropriate number of digits
    sum = 0
    for i in range(k):
        n = len(str(arr[i]))
        if n <= 2:
            sum += arr[i]

    return sum


# test cases
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
print(add_elements([100, 100, 100], 2))
print(add_elements([1, 2, 3, 4, 5], 5))
print(add_elements([21, 3, 4000, 5, 6, 7, 8, 9], 4))
print(add_elements([1, 2, 3, 4, 5], 2))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 2))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 3))
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1))
