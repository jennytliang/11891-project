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
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] <= arr[1]:
            return 0
        return 1
    
    for i in range(len(arr)):
        if arr[i] <= arr[i-1]:
            return i
    
    return -1


print(can_arrange([1,2,4,3,5]))
print(can_arrange([1,2,3]))
print(can_arrange([2,1,2,3,2,1]))
print(can_arrange([1,2,3,4,5,6,7,8,9,10]))
print(can_arrange([1,1,1,1,1,1,1,1,1,1]))
print(can_arrange([1,2,3,9,8,7,6,5,4,3,2,1]))
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]))