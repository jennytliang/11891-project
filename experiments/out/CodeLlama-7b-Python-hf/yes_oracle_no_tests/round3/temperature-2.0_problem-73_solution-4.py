def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: , c nt
	"""

    arr_rev = arr[::-1]
    arr_zip = list(zip(arr, arr_rev))
    palindrome = [c for c in arr_zip if c[0] == c[1]]
    return len(arr) - len(palindrome)


def smallest_change_2(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: , c nt
	"""

    palindrome = arr[::]
    for i in range(len(arr)//2):
        if arr[i] != palindrome[-(i+1)]:
            palindrome[i] = palindrome[-(i+1)]

    palindrome_set = set(palindrome)
    palindrome_count = len(palindrome_set)

    return len(arr) - palindrome_count


print(smallest_change([1,2,3,5,4,7,9,6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))

print(smallest_change_2([1,2,3,5,4,7,9,6]))
print(smallest_change_2([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change_2([1, 2, 3