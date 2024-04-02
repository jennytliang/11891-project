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
    if len(arr) == 1 and k == 1:
        return arr[0]
    elif len(arr) == 1 and k == 0:
        return 0
    elif len(arr) == 0 and k == 0:
        return 0
    elif len(arr) == 0 and k > 0:
        return 0
    else:
        return add_elements(arr[:k], k) + add_elements(arr[k:], k)


def digits(x):
    """
    Return the number of digits in the input number.
    """
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
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    if len(arr) == 1 and k == 1:
        return arr[0]
    elif len(arr) == 1 and k == 0:
        return 0
    elif len(arr) == 0 and k == 0:
        return 0
    elif len(arr) == 0 and k > 0:
        return 0
    else:
        if digits(arr[k - 1]) > 2:
            return add_elements_2(arr[:k], k)
        else:
            return add_elements_2(arr[:k], k) + add_elements_2(arr[k:], k)

