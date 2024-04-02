def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len ( arr ) -
	"""
    # TODO: Write your solution here
    # 1, 2, 4, 3, 5
    # 1, 1, 2, 3, 4
    # 1, 1, 2, 2, 3
    # 1, 1, 2, 2, 2
    # 1, 1, 2, 2, 2, 3
    # 1, 1, 2, 2, 2, 2
    # 1, 1, 2, 2, 2, 2, 3
    # 1, 1, 2, 2, 2, 2, 2
    # 1, 1, 2, 2, 2, 2, 2, 3
    largest = 0
    for i in range(len(arr)):
        if arr[i] >= arr[largest]:
            largest = i
    if largest == len(arr) - 1:
        return -1
    return largest


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
