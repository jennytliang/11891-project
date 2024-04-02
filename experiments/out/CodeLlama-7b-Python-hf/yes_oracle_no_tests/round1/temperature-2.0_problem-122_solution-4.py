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
    # sum = 0
    # for i in range(k):
    #     if digits(arr[i]) <= 2:
    #         sum += arr[i]
    # return sum
    return sum(arr[i] for i in range(k) if digits(arr[i]) <= 2)


def digits(x : int) -> int:
    """
    Return the number of digits of x
    """
    if x == 0:
        return 1
    return len(str(x))


def add_elements_2(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
    """
    return sum(arr[i] for i in range(k) if 1 <= arr[i] <= 99)


def add_elements_3(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
    """
    return sum(arr[i] for i in range(k) if 1 <= arr[i] <= 99)


def add_elements_4(arr, k):
