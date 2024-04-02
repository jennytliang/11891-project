def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Sort the input , so
	"""
    arr.sort()
    prev = -1
    for i, n in enumerate(arr):
        if n < prev:
            return i - 1
        prev = n
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
print(can_arrange([1, 1, 2, 3]))
print(can_arrange([1, 2, 3, 3]))
print(can_arrange([1, 2, 3, 3, 4]))
print(can_arrange([1, 2, 3, 3, 4, 4]))
print(can_arrange([1, 2, 3, 3, 4, 4, 5]))
print(can_arrange([1, 2, 3, 3, 4, 4, 5, 6]))
print(can_arrange([1, 2, 3, 3, 4, 4, 5, 6, 6]))
print(can_arrange([1, 2, 3, 3, 4, 4, 5, 6, 6, 7]))
