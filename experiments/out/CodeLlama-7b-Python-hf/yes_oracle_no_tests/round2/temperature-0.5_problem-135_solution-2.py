def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: n = len ( arr )
	"""
    # Your code here
    if len(arr) < 2:
        return -1
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return -1
        else:
            return 0
    else:
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                return i
        return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
print(can_arrange([1, 3, 2]))
print(can_arrange([1, 2, 3, 2, 1]))
print(can_arrange([1, 2, 3, 4, 5]))
print(can_arrange([1, 2, 3, 4, 3]))
print(can_arrange([1, 2, 3, 2, 4]))
print(can_arrange([1, 2, 3, 4, 5, 6]))
print(can_arrange([1, 2, 3, 4, 5, 5]))
print(can_arrange([1, 2, 3, 4, 5, 4]))
print(can_arrange([1, 2, 3, 4, 5, 3]))
print(can_arrange([1, 2, 3, 4, 5, 2]))
print(can_arrange([1, 2, 3, 4, 5, 1]))
print(can_arrange([1, 2, 3, 4, 5, 1, 2]))
print(can_arrange([1, 2, 3, 4, 5, 1, 2, 3]))
print(can_arrange([1, 2, 3, 4, 5, 1, 2, 3, 4]))
print(can_ar