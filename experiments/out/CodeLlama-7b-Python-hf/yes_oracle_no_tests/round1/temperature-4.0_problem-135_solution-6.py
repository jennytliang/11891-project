def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Sort the input , so
	"""
    if len(arr) == 0 or len(arr) == 1:
        return -1
    else:
        sorted_arr = list(sorted(arr))
        for i, num in enumerate(sorted_arr):
            if num < sorted_arr[i-1]:
                return i-1
        return -1


if __name__ == "__main__":
    arr = [1,2,4,3,5]
    print(can_arrange(arr))
    arr = [1,2,3]
    print(can_arrange(arr))
