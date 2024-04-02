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
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    
    re_arr = arr[::-1]
    sum = 0
    
    for i in range(len(re_arr)):
        cnt = 0
        for j in range(i,len(re_arr)):
            if (arr[i] == arr[j]):
                cnt += 1
                break
            else:
                cnt += 1
        sum += (i+i+cnt-len(re_arr))
    return sum

    # pass
    
smallest_change([1,2,3,5,4,7,9,6])