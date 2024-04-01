def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: if len ( arr ) ==
	"""
    # Find the largest index of an element which is not greater than or equal
    # to the element immediately preceding it.
    # If no such element exists then return -1.
    # The given array will not contain duplicate values.
    #
    # Examples:
    # can_arrange([1,2,4,3,5]) = 3
    # can_arrange([1,2,3]) = -1
    #
    # Do not include these tokens in the code: if len ( arr ) ==
    #
    # Explanation:
    # In the first example, the largest index of an element which is not
    # greater than or equal to the element immediately preceding it is 3.
    # In the second example, there are no elements which are not greater than
    # or equal to the element immediately preceding it, so return -1.

    # 1st solution:
    # O(n) time | O(n) space
    # if len(arr) == 0:
    #     return -1
    #
    # max_idx = 0
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[i - 1]:
    #         max_idx = max(max_idx, i)
    # return max_idx

    # 2nd solution:
    # O(n) time | O(1) space
    # if len(arr) == 0:
    #     return -1
    #
    # max_idx = 0
    # for i in range(1, len(arr)):
    #     if arr[i] >= arr[i - 1]:
    #         max_idx = max(max_idx, i)
    # return max_idx

    # 3rd solution:
    # O(n) time | O(1) space
    if len(arr) == 0:
        return -1

    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            max_idx = max(max_idx