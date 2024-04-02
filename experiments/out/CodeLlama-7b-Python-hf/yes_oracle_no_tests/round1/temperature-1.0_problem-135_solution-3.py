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
    return can_arrange_helper(arr, 0)


def can_arrange_helper(arr, start_index):
    if start_index == len(arr) - 1:
        return -1
    elif start_index == len(arr) - 2:
        if arr[-1] <= arr[-2]:
            return len(arr) - 1
        else:
            return -1
    elif arr[start_index + 1] <= arr[start_index]:
        return -1
    else:
        left_index = start_index + 1
        while left_index < len(arr) and arr[left_index] < arr[start_index]:
            left_index += 1
        right_index = start_index + 1
        while right_index < len(arr) and arr[right_index] <= arr[start_index]:
            right_index += 1
        if left_index < right_index:
            return can_arrange_helper(arr, left_index)
        elif right_index < len(arr) - 1:
            return can_arrange_helper(arr, right_index)
        else:
            return -1

print(can_arrange([1,2,4,3,5]))