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
    # init variables
    sum_of_two_digits = 0
    # sum_of_two_digits = sum(arr[:k])

    # sum_of_two_digits = sum_of_two_digits + sum([i for i in arr[:k] if digits(i) < 3])

    # return sum_of_two_digits
    return sum(arr[:k]) + sum([i for i in arr[:k] if digits(i) < 3])


def digits(x):
    """
    Returns the number of digits in an integer
    """
    s = str(x)
    return len(s)


print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))
