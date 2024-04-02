def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # re create the array in
	"""
    # check if array is palindrome, if so return 0
    if arr == arr[::-1]:
        return 0
    # create two pointers for start and end of array
    start = 0
    end = len(arr) - 1
    # create a counter to keep track of the number of changes
    counter = 0
    # while start is less than end
    while start < end:
        # if the start and end elements are not the same
        if arr[start] != arr[end]:
            # increment the counter
            counter += 1
            # set the start value to the same as the end value
            arr[start] = arr[end]
        # decrement the start value and increment the end value
        start += 1
        end -= 1
    return counter
