def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # TODO : Write your solution here
	"""
    # TODO : Write your solution here
    for i in range(len(arr)):
        if i == 0:
            if arr[i] <= arr[i+1]:
                return arr[i]
        elif i == len(arr)-1:
            if arr[i] <= arr[i-1]:
                return arr[i]
        elif arr[i] <= arr[i-1] and arr[i] <= arr[i+1]:
            return arr[i]
    return -1


def can_arrange_2(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # TODO : Write your solution here
	"""
    # TODO : Write your solution here
    for i in range(len(arr)):
        if i == 0:
            if arr[i] <= arr[i+1]:
                return arr[i]
        elif i == len(arr)-1:
            if arr[i] <= arr[i-1]:
                return arr[i]
        elif arr[i] <= arr[i-1] and arr[i] <= arr[i+1]:
            return arr[i]
    return -1
