def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # Check if array is already pal
	"""
    # Your code here
    # palindrome = is_palindrome(arr)
    # if palindrome:
    #     return 0
    # else:
    #     return smallest_change(arr)
    # palindrome = is_palindrome(arr)
    # if palindrome:
    #     return 0
    # else:
    #     return smallest_change(arr)
    # palindrome = is_palindrome(arr)
    # if palindrome:
    #     return 0
    # else:
    #     return smallest_change(arr)
    # palindrome = is_palindrome(arr)
    # if palindrome:
    #     return 0
    # else:
    #     return smallest_change(arr)
    palindrome = is_palindrome(arr)
    if palindrome:
        return 0
    else:
        return smallest_change(arr)


def is_palindrome(arr):
    # arr = list(arr)
    # # arr = arr[::-1]
    # for i in range(len(arr)):
    #     if arr[i] != arr[len(arr) - i - 1]:
    #         return False
    # return True
    return is_palindrome_recur(arr, 0)


def is_palindrome_recur(arr, i):
    if i >= len(arr):
        return True
    else:
        return arr[i] == arr[len(arr) - i - 1] and is_palindrome_recur(arr, i + 1)


# print(is_palindrome([1, 2, 3, 5, 4, 7, 9, 6]))
# print(is_palindrome([1, 2, 3, 4, 3, 2, 2]))
# print(is_palindrome([1, 2, 3, 2, 1]))
print(smallest_change([1, 2, 3, 