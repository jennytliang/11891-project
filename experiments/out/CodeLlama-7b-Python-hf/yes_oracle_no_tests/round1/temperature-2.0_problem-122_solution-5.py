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
    # 1 <= len(arr) <= 100
    # 1 <= k <= len(arr)
    # 1 <= x <= 9
    # 2 <= k <= len(arr)

    # arr = [111,21,3,4000,5,6,7,8,9]
    # k = 4

    # x = 111
    # digits(x)
    # 3

    # x = 21
    # digits(x)
    # 2

    # x = 4000
    # digits(x)
    # 4

    # sum = 24

    # arr = [111,21,3,4000,5,6,7,8,9]
    # k = 4
    # max_digits = 2
    # count = 0
    # sum = 0
    # for i in range(k):
    #     x = arr[i]
    #     count += 1
    #     if digits(x) <= max_digits:
    #         sum += x
    # return sum

    # return sum

    max_digits = 2
    count = 0
    sum = 0
    for i in range(k):
        x = arr[i]
        count += 1
        if digits(x) <= max_digits:
            sum += x
    return sum


def digits(x):
    """
    Return the number of digits in an integer
    """
    return len(str(abs(x)))


def add_elements_solution(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

