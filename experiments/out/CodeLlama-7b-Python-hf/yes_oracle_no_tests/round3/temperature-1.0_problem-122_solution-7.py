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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # find the length of the array
	"""
    # check that the length of the array is at least k
    if len(arr) < k:
        raise ValueError("The length of the array must be greater than k")

    # initialize the sum to 0
    sum_of_elements = 0

    # loop through the first k elements of the array
    for i in range(k):
        # check if the element has 2 digits or less
        if len(str(arr[i])) <= 2:
            # add the element to the sum
            sum_of_elements = sum_of_elements + arr[i]

    return sum_of_elements


# # test add_elements()
# arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
# k = 4
# print(add_elements(arr, k))


def add_elements_two(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # find the length of the array
	"""
    # check that the length of the array is at least k
    if len(arr) < k:
        raise ValueError("The length of the array must be greater than k")

    # initialize the sum to 0
    sum_of_elements = 0

    # loop through the first k elements of the array
    for i in range(k):
        # check if the element has 2 digits or less
        if len(str(arr[i])) <=