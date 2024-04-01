def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # If the array is empty
	"""
    if not arr:
        return 0
    
    # If the array is a palindrome
    if arr == arr[::-1]:
        return 0
    
    # If the array is not a palindrome, we need to find the first index where the array is not a palindrome
    # and then we need to find the minimum number of changes to make the array a palindrome
    for i in range(len(arr)):
        if arr != arr[::-1]:
            # We need to find the minimum number of changes to make the array a palindrome
            return len(arr) - i
        
    return len(arr)


# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
