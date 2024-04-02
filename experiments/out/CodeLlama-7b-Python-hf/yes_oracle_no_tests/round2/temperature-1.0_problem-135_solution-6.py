def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: from collections import default dict
	"""
    d = {0:-1}    # dictionary to store the index of the largest number not greater than or equal to the number preceding
    for i in range(len(arr)):
        if arr[i] <= arr[i - 1]:
            d[arr[i]] = i
        else:
            d[arr[i]] = -1
            
    #returning the largest index
    max_i = max(d.values())
    return max_i
            
              

    
    

    
