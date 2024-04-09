def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # check if input array is pal
	"""
    # check if input array is pal
    if arr == arr[::-1]:
        return 0

    # get the length of the array
    length = len(arr)

    # get the number of palindromes
    palindromes = 0

    # loop through the array
    for i in range(length):
        # if the first element is the last, add 1 to palindrome
        if arr[i] == arr[length - 1 - i]:
            palindromes += 1

    # return the length of the array minus the number of palindromes
    return length - palindromes


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
