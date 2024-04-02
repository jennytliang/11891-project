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
    #check edge cases
    if len(arr) <= 1:
        return 0
    
    #create a reversed copy of the array
    arr_reversed = arr[::-1]
    
    #create a counter
    cnt = 0
    
    #iterate over the array
    for i in range(len(arr)):
        
        #if the element is not equal to the reversed element, increment the counter
        if arr[i] != arr_reversed[i]:
            cnt += 1
            
    return cnt

#test
arr = [1,2,3,5,4,7,9,6]
print(smallest_change(arr)) #4

arr = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr)) #1

arr = [1, 2, 3, 2, 1]
print(smallest_change(arr)) #0
