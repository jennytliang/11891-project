def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Sort the input, so we have the index
    # to the original indices in arr
    sorted_arr = sorted(i for i in range(len(arr))).index(arr[ind])


    return # Expected return value below
    # Your code here.
    
    
print(can_arrange(4, 6, -2, 3, 12, 7))