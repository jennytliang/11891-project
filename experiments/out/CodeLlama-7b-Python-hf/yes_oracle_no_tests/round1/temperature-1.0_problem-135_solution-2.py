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
    def can_arrange_index(a):
	    
        output = arr[0]
        for i in range(1, len(arr), 1):
            if (arr[i] != output):
                diff = arr[i] - output - 1
                if diff < 0:
                    return -1

                output = arr[i] + diff
        return (len(arr)-1)

    return can_arrange_index
