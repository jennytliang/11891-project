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
	Do not include these tokens in the code: if len ( ) <
	"""
    # iterate through array - find a reversion in the array
    reversed = arr[::-1]
    palindrome = False
    reversed_index = 0 # 
    for i in range(len(arr)):
        if arr[i] != reversed[reversed_index]:
            palindrome = False
            cnt = calculate_changes(arr, reversed, reversed_index)
            break
        else:
            palindrome = True
    if palindrome:
        return 0
    else:
        return cnt

def calculate_changes(arr, reversed, reversed_index):   
    cnt = 0
    for i in range(0, reversed_index + 1):
        if arr[i] != reversed[reversed_index - i]:
            cnt += 1
    return cnt




smallest_change([1,2,3,5,4,7,9,6])
smallest_change([1, 2, 3, 4, 3, 2, 2])
smallest_change([1, 2, 3, 2, 1])