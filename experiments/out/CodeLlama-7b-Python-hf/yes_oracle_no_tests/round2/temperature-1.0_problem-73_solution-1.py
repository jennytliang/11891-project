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
	"""
    i = 0
    j = len(arr)-1
    min_ch = len(arr) - 1
    while i<=j:
        if arr[i] == arr[j]:
            i+=1
            j-=1
        elif cnt[arr[i]] < cnt[arr[j]]:
            i+=1
            min_ch-=1
        else:
            j-=1
            min_ch-=1
        return min_ch
    
