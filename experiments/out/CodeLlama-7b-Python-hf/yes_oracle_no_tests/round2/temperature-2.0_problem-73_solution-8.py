def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # First , we ' ll reverse
	"""
    # First , we ' ll reverse
    arr.reverse()

    # we ' ll create an empty list with the same size as the arr
    new_arr = [0] * len(arr)

    # we ' ll iterate over the arr
    for i in range(len(arr)):
        # and we ' ll add the elements of the arr to the new_arr
        new_arr[i] = arr[i]

    # we ' ll store the result
    result = 0

    # we ' ll iterate over the new_arr
    for i in range(len(new_arr)):
        # we ' ll check if the element is equal to the element in the arr
        if new_arr[i] == arr[i]:
            # we ' ll do nothing
            continue
        else:
            # we ' ll increment the result
            result += 1

    return result


print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
