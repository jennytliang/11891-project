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
    # first we need to make the arr a palindrome
    # we do this by reversing it
    # then we use two pointers to compare the two halves of the array
    # if they are not equal, we keep track of the number of changes
    # then we return the number of changes
    cnt = arr
    cnt.reverse()
    changes = 0
    for i in range(int(len(arr) / 2)):
        if arr[i] != cnt[i]:
            changes += 1
    return changes


print(smallest_change([1,2,3,5,4,7,9,6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
