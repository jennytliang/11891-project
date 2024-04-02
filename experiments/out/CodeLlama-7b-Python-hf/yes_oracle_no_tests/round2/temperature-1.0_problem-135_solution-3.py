def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: n = len ( arr
	"""
    if len(arr) == 0:
        return 0
    elif len(arr) % 2 == 0:
        return 0
    else:
        sum = 0
        for a in range(len(arr)):
            sum += arr[a]
        return sum
        
   
