def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers
	Do not include these tokens in the code: # iterate through array - find a
	"""
    if arr == arr[::-1]:
        return 0
    count = 0
    newArr = []
    rev = arr[::-1]
    for i in range(0, len(arr) - 1):
        if(arr[i] != rev[i]):
            count +=1
            newArr.append(rev[i])
    for idx, item in enumerate(arr):
        if count == len(newArr):
            break
        arr[idx] = newArr[0]
        count -=1
        newArr.remove(newArr[0])
    return count

    
    