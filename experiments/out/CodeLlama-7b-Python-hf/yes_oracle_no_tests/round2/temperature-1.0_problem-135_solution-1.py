def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: _ max = max ( arr )
	"""
        
    if not arr:
        return -1

    max_num = max(arr)
    prev_index = -2
    max_index = -1
    curr_index = -1

    found = False

    for num in arr:
        if num < max_num and not found and num >= arr[curr_index + 1] + 1:
            found = True
            max_index = curr_index + 1
            #prev_index = curr_index

        if not (num < arr[prev_index + 1]):
            if num >= arr[prev_index + 1] + 1:
                return -1
                #found = False

            if arr[prev_index + 1] > max_num:
                max_index = prev_index + 1
                max_num = arr[prev_index + 1]

        curr_index += 1
        prev_index += 1

    if found:
        return max_index

    return -1
