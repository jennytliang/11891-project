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
    # if k == 0:
    #     return 0
    # if k == 1:
    #     return sum(arr)

    # # add first k elements
    # total = 0
    # for i in range(k):
    #     total += arr[i]

    # # add the next k elements
    # for i in range(k, len(arr)):
    #     if digits(arr[i]) <= 2:
    #         total += arr[i]

    # return total

    # # add first k elements
    # total = 0
    # for i in range(k):
    #     total += arr[i]

    # # add the next k elements
    # for i in range(k, len(arr)):
    #     if digits(arr[i]) <= 2:
    #         total += arr[i]

    # return total

    # # add first k elements
    # total = 0
    # for i in range(k):
    #     total += arr[i]

    # # add the next k elements
    # for i in range(k, len(arr)):
    #     if digits(arr[i]) <= 2:
    #         total += arr[i]

    # return total

    # # add first k elements
    # total = 0
    # for i in range(k):
    #     total += arr[i]

    # # add the next k elements
    # for i in range(k, len(arr)):
    #     if digits(arr[i]) <= 2:
    #         total += arr[i]

    # return total

    total = 0
    for i in range(k):
        total += arr[i]

    for i in range(k, len(arr)):
        if digits(arr[i]) <= 2:
            total += arr[i]

    return total


def digits(x: int) -> int:
    """
    Count the number of digits in a number
    """
    if x == 0:
       