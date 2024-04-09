def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # your code here if
	"""
    # your code here
    n = len(arr)
    # check if array is palindrome
    if arr == arr[::-1]:
        return 0
    
    # check if array is palindrome with one swap
    for i in range(n-1):
        if arr[i] == arr[n-1-i]:
            continue
        else:
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
            if arr == arr[::-1]:
                return 1
            else:
                arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    
    # check if array is palindrome with two swaps
    for i in range(n-2):
        if arr[i] == arr[n-2-i]:
            continue
        else:
            arr[i], arr[n-2-i] = arr[n-2-i], arr[i]
            if arr == arr[::-1]:
                return 2
            else:
                arr[i], arr[n-2-i] = arr[n-2-i], arr[i]
    
    # check if array is palindrome with three swaps
    for i in range(n-3):
        if arr[i] == arr[n-3-i]:
            continue
        else:
            arr[i], arr[n-3-i] = arr[n-3-i], arr[i]
            if arr == arr[::-1]:
                return 3
            else:
                arr[i], arr[n-3-i] = arr[n-3-i], arr[i]
    
    # check if array is palindrome with four swaps
    for i in range(n-4):
        if arr[i] == arr[n-4-i]:
            continue
        else:
            arr[i], arr[n-4-i] = arr[n-4-i], arr[i]
            if arr == arr[::-1]:
               