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
    if len(arr) == 0:
        return 0
    if k == 0:
        return 0
    if k > len(arr):
        return sum(arr)

    sum_two_digits = 0
    for i in range(k):
        sum_two_digits += digits(arr[i])

    return sum_two_digits


def digits(x):
    """
    Given a non-negative integer x, return the number of digits in x.
    """
    if x == 0:
        return 1
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count


def test_add_elements():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([1, 2, 3], 3) == 6
    assert add_elements([1, 2, 3], 2) == 5
    assert add_elements([1, 2, 3], 1) == 3
    assert add_elements([1, 2, 3], 0) == 0
    assert add_elements([1, 2, 3], 4) == 6
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1) == 3
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 2) == 21
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 3) == 24
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8