def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # Check if the array is already
	"""
    # for _ in range(len(arr)):
    #     if arr[0] == arr[len(arr) - 1]:
    #         arr.pop(0)
    #         arr.pop(len(arr) - 1)
    #     else:
    #         arr.remove(arr[0])
    #         arr.remove(arr[len(arr) - 1])
    #         arr.insert(0, arr[len(arr) - 1])
    #         arr.insert(len(arr) - 1, arr[0])
    # return len(arr)
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] != arr[end]:
            arr.pop(start)
            arr.pop(end)
            arr.insert(start, arr[end])
            arr.insert(end, arr[start])
            start += 1
            end -= 1
        else:
            start += 1
            end -= 1
    return len(arr)


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
