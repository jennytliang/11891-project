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

    # We maintain two pointers to the array from opposite ends and move them
    # towards each other.
    #
    # Let's denote leftptr to leftmost index i at the first index of the loop 
    # and rightptr to rightmost index j at the second index.
    #
    # Then loop invariant is
    # 
    # j - leftptr + 1 >= n
    # for all i, j < n. (i.e. both pointers are within the array)
    #
    # We break this loop when j reaches leftptr (if no such element found).
    # Otherwise, we find the number in arr[j] that is smaller than in
    # arr[leftptr - 1] and return j.

    leftptr = 0
    rightptr = len(arr) - 1
    
    while leftptr < rightptr and rightptr - leftptr + 1 >= len(arr):
        if arr[leftptr] <= arr[rightptr]:
            return rightptr

        leftptr += 1
        while leftptr < rightptr and arr[rightptr] >= arr[leftptr]:
            rightptr -= 1

    return -1
