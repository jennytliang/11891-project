def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt = arr
	"""
    # Initialize the variables
    re_arr = []
    cnt = 0
    # Loop through the array
    for idx, num in enumerate(arr):
        # If the number is equal to the reversed array, skip it
        if num == arr[len(arr) - idx - 1]:
            continue
        # If the number is not equal to the reversed array, add it to the new array
        else:
            re_arr.append(num)
            cnt += 1
    return cnt


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
