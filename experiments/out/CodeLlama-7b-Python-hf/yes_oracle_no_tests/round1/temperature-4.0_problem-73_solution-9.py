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
    #reversed_arr = arr[::-1]
    #for i in range(len(arr)):
    #    if arr[i] != reversed_arr[i]:
    #        cnt += 1
    
    #return cnt
    
    # arr = [1,2,3,5,4,7,9,6]
    # reversed_arr = [6,9,7,4,5,3,2,1]
    # cnt = 0
    # for i in range(len(arr)):
    #     if arr[i] != reversed_arr[i]:
    #         cnt += 1
    # return cnt
    
    # arr = [1, 2, 3, 4, 3, 2, 2]
    # reversed_arr = [2, 2, 3, 4, 3, 2, 1]
    # cnt = 0
    # for i in range(len(arr)):
    #     if arr[i] != reversed_arr[i]:
    #         cnt += 1
    # return cnt
    
    # arr = [1, 2, 3, 2, 1]
    # reversed_arr = [1, 2, 3, 2, 1]
    # cnt = 0
    # for i in range(len(arr)):
    #     if arr[i] != reversed_arr[i]:
    #         cnt += 1
    # return cnt
    
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # reversed_arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9,