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
    result = [arr[0],-1]
    for i in range(1, len(arr)):
        if arr[i] > result[i-1] and arr[i] < max(arr[i-1], result[0]):
            result[0] = arr[i]
            result[i] = i
        elif arr[i] == arr[i-1]:
            result[i] = -1
        elif arr[i] > max(arr[i-1], result[0]):
            result[i] = -1
        elif arr[i] == arr[0]:
            result[0] = arr[i]
    return result[1]