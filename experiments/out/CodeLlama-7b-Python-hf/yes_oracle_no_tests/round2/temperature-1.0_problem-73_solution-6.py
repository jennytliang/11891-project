def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed
	Do not include these tokens in the code: ### #### #
	"""
    _re = {}
    for i in range(len(arr)//2):
        if arr[i] in _re:
            _re[arr[i]] += 1
        else:
            _re[arr[i]] = 1
            
    for i in range(len(arr)//2)[::-1]:
        if arr[i] in _re:
            _re[arr[i]] += 1
        else:
            _re[arr[i]] = 1
            
    _reversed = {}
    for i in range(len(arr)//2):
        if arr[~i] in _reversed:
            _reversed[arr[~i]] += 1
        else:
            _reversed[arr[~i]] = 1
    
    for key, value in _reversed.items():
        if key == key+1 and key != 1 and value > _re[key]:
            return value - _re[key]
    
    return 0