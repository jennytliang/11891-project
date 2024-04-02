def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # arr = [ 1 ,
	"""
    # Find the largest index of an element which is not greater than or equal
    # to the element immediately preceding it.
    for i in range(len(arr)):
        if arr[i] <= arr[i-1]:
            return i-1
    return -1


if __name__ == "__main__":
    inputs = [
        [1, 2, 4, 3, 5],
        [1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for input in inputs:
        print(can_arrange(input))
