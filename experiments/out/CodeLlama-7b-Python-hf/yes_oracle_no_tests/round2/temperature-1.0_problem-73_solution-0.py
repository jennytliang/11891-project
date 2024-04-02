def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: if len ( )
	"""
    # iterate through list backwards in pairs, find index of equal value, 
    # then iterate backwards from last index and find first index equaling value.
    # compare distance between both by subtracting each and adding 1 to first value.
    #return value.
    length = len(arr)
    backToLength = length // 2
    total = 0
    maxLength = 0
    maxValue = max(arr)
    for i in range(backToLength):
        start = arr[i]
        end = arr[length - i - 1]
        
        startVal = start
        endVal = end
        
        for j in range(backToLength):
            if (start == arr[j]) and (end == arr[length - j - 1]):
                break

        if (start >= endVal) and (end >= startVal):
            total += (end - start)
        elif (startVal >= end) and (endVal >= start):
            total += (start - end)
        else:
            total += min(start - endVal, end - startVal)

        if maxLength < abs(max(start, end) - min(start, end)):
            maxLength = abs(max(start, end) - min(start, end))
            
    total += maxLength
    return total

