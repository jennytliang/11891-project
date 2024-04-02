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
    # Check if array is already palindrome
    if arr == arr[::-1]:
        return 0

    # Find array length
    n = len(arr)

    # Initialize two pointers, one starting at the beginning of the array,
    # the other starting at the end of the array
    i = 0
    j = n - 1

    # Initialize a variable to keep track of the number of changes required
    # to make the array palindromic
    changes = 0

    # Iterate through the array
    while i < j:
        # Check if the left element is the same as the right element
        if arr[i] == arr[j]:
            # If it is, move both pointers one step to the right
            i += 1
            j -= 1
        else:
            # If it is not, check if the left element is greater than the
            # right element
            if arr[i] > arr[j]:
                # If it is, move the left pointer one step to the right
                i += 1
                changes += 1
            else:
                # If it is not, move the right pointer one step to the left
                j -= 1
                changes += 1

    # Return the number of changes required to make the array palindromic
    return changes
