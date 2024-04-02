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
    arr_reversed = arr[::-1] # arr reversed
    for idx, val in enumerate(arr):
        if arr_reversed[idx] != val:
            cnt = 0 # cnt = arr, cnt = 0
            for idx1 in range(idx + 1, len(arr) - idx): # idx1 = idx + 1, idx1 = len (arr) - idx
                cnt += 1
                if arr_reversed[idx1] == val:
                    return cnt
        
        # [1, 2, 3, 4, 3, 2, 2]
        # idx = 3
        # 3 == 3, 2 == 3, cnt = 0
        # [1, 2, 3, 3, 3, 2, 2]
        # idx1 = 4
        # cnt = 1
        # [1, 2, 3, 3, 2, 2, 2]
        # idx1 = 5
        # cnt = 2
        # [1, 2, 3, 3, 2, 2, 2]
        # idx = 6
        # 3 == 2, cnt = 3

        # [1, 2, 3, 4, 3, 2, 2]
        # idx = 3
        # 4 == 3, 2 == 2, cnt = 0
        # [1, 2, 3, 3, 3, 2, 2]
        # idx1 = 4
        # cnt = 1        
        # [1, 1, 3, 3, 2, 2, 2]        
        # idx = 6
        # 2 == 1, cnt = 2
    return 0



print(smallest_change([1,2,3]))  # 2
print(smallest_change([1,2,3,4,3,2,2])) # 1
print(smallest_