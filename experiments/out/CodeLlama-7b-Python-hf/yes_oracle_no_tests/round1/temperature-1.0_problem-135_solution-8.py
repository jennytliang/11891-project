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
    for i in range(len(arr)):
        if arr[i] > arr[len(arr)-1]:
            return -1
    else:
        for i in range(len(arr)-1):
            arr.append(-1)
            if arr[i] > arr[len(arr)-1]:
                del arr[-1]
            j = i
            for i in range(i, j):
                if arr[i] < arr[j]:
                    arr[j] = arr[j] - arr[j+1]
            return arr.index((arr[0]))
