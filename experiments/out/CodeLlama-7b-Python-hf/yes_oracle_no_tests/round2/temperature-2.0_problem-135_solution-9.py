def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: ) - 1 , 0 , -
	Do not include these tokens in the code: )-
	"""

    for i in range(le(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i] and j <= arr[i]:
                return j
    return -1
