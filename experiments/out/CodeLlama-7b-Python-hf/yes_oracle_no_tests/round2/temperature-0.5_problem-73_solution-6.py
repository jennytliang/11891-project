def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: # TODO : Write a recursive
	"""
    # TODO : Write a recursive
    def recurse(arr, current):
        if len(arr) == 0:
            return current
        elif len(arr) == 1:
            return 0
        elif len(arr) == 2:
            if arr[0] == arr[1]:
                return 0
            else:
                return 1
        else:
            if arr[0] == arr[len(arr) - 1]:
                return recurse(arr[1:len(arr) - 1], current)
            else:
                return 1 + recurse(arr[1:len(arr) - 1], current)
    return recurse(arr, 0)


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
