def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt
	Do not include these tokens in the code: # Find the number of elements in
	"""
    # Your code here
    # re_arr = arr[::-1]
    # print(re_arr)
    # for i in range(len(arr)):
    #     if arr[i] != re_arr[i]:
    #         cnt += 1
    # print(cnt)

    # 1 2 3 4 3 2 2
    # 1 2 3 4 5 6 7
    # 1 2 3 3 2 1
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7

    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2
    # 1 2 3 4 3 2 2

    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7
    #