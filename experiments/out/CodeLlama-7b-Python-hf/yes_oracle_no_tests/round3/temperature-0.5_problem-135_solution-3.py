def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Write your code here
	"""
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return 0
    elif arr[1] <= arr[0]:
        return 0
    
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1] and arr[i] <= max_index:
            max_index = i
    if max_index == 0:
        return 0
    else:
        return max_index


# Tests
def can_arrange_test(test_case):
    print("Pass" if (can_arrange(test_case[0]) == test_case[1]) else "Fail")


can_arrange_test([[1,2,4,3,5], 3])
can_arrange_test([[1,2,3], -1])
can_arrange_test([[2,3,4,5,6], 4])
can_arrange_test([[1,1,1,1], 0])
can_arrange_test([[1,3,5,7,9], 2])
