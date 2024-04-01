def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    """ALGORITHM"""
    ## Base Case:
    if len(set(arr)) == 1: return -1

    ## HINT:
    ## Since we are given that there are not duplicate values, we can use
    ## the fact that arr is in sorted order to perform our searching.
    ## We will be looking for the largest index such that the element
    ## immediately preceding it is smaller than or equal to its value.

    result = -1
    for i, num in enumerate(arr):
        if arr[i-1] <= num:
            result = i

    return result
        