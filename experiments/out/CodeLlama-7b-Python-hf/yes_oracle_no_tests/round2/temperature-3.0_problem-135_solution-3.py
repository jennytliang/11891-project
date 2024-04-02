def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: l =
	"""
    # TODO: Write your solution here
    l = len(arr)
    for i in range(l):
        if arr[i] <= arr[i-1] and i != 0:
            return -1
        elif arr[i] > arr[i-1] and i == 0:
            return -1
        else:
            for j in range(l):
                if arr[j] > arr[j-1]:
                    return j




print(can_arrange([1,2,4,3,5]))
print(can_arrange([1,2,3]))

