def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt
	Do not include these tokens in the code: result
	"""
    # Reverse the array
    arr_reversed = arr[::-1]
    # Create a new array
    arr_new = []
    # Loop through the original array and the reversed array
    for i in range(len(arr)):
        # If the element from the original array is equal to the element from the reversed array
        if arr[i] == arr_reversed[i]:
            # Add the element from the original array to the new array
            arr_new.append(arr[i])
        # If the element from the original array is not equal to the element from the reversed array
        else:
            # Add the element from the reversed array to the new array
            arr_new.append(arr_reversed[i])
    # Initialize a counter variable
    cnt = 0
    # Loop through the new array
    for i in range(len(arr_new)):
        # If the element from the original array is not equal to the element from the new array
        if arr[i] != arr_new[i]:
            # Increment the counter variable
            cnt += 1
    # Return the counter variable
    return cnt