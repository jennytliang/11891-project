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
	Do not include these tokens in the code: # Re verse the array
	"""
    arr_reversed = arr[::-1]
    # Reverse the array
    arr_reversed = list(map(str, arr_reversed))
    arr = list(map(str, arr))
    # Make the array strings
    new_arr = []
    # Create empty array
    for i in range(len(arr)):
        new_arr.append(arr[i] + arr_reversed[i])
        # Append the two arrays together
    new_arr = list(map(int, new_arr))
    # Convert the array to integers
    new_arr.sort()
    # Sort the array
    cnt = 0
    # Create a counter
    for i in range(1, len(new_arr)):
        if new_arr[i] == new_arr[i - 1]:
            cnt += 1
            # Add to the counter if the numbers are the same
    return cnt


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
