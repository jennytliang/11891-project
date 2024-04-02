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
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: # Add your code here
	"""

    # Add your code here
    if k == 0:
        return 0
    else:
        return sum(arr[:k])


def add_elements_v2(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: # Add your code here
	"""

    # Add your code here
    return sum(arr[:k])


assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
assert add_elements([111,21,3,4000,5,6,7,8,9], 3) == 24
assert add_elements([111,21,3,4000,5,6,7,8,9], 2) == 12
assert add_elements([111,21,3,4000,5,6,7,8,9], 1) == 6
assert add_elements([111,21,3,4000,5,6,7,8,9], 0) == 0
assert add_elements([111,21,3,4000,5,6,7,8,9], 10) == 45

assert add_elements_v2([111,21,3,4000,5,6,7,8,9], 4) == 24
assert add_elements