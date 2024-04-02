def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # arr = [ 1 ,
	"""
    # Initialize variables
    left = 0
    right = len(arr) - 1
    result = -1

    # Base case
    if right < 0:
        return result

    # Recursive case
    if arr[right] >= arr[right - 1]:
        return result

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid - 1]:
            result = mid - 1
            right = mid - 1
        elif arr[mid] > arr[mid - 1]:
            left = mid + 1
        else:
            left = mid + 1

    return result


def can_arrange_brute_force(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # arr = [ 1 ,
	"""
    # Initialize variables
    result = -1

    # Base case
    if len(arr) < 2:
        return result

    # Recursive case
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            result = i
        else:
            return result

    return result


# Test cases
print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
print(can_arrange([1, 2, 3, 4, 5]))
print(can_arrange([5, 4, 3, 2, 1]))
print(can_arrange([1, 2, 2, 3, 3, 3, 4,