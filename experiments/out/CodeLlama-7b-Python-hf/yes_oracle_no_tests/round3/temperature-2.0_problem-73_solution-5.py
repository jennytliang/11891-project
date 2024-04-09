def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # Your code here if
	"""
    # 1st solution
    # O(n) time | O(n) space 
    # where n is the length of the input array
    def smallest_change(arr):
        # for each index in the array
        # check the next index
        # if they are not equal
        # add 1 to the result
        # return the result
        result = 0
        for i in range(len(arr)):
            if i + 1 < len(arr):
                if arr[i] != arr[i + 1]:
                    result += 1
        
        return result
    
    return smallest_change(arr)
    
    # 2nd solution
    # O(n) time | O(n) space
    # where n is the length of the input array
    def smallest_change(arr):
        # for each index in the array
        # check the next index
        # if they are not equal
        # add 1 to the result
        # return the result
        result = 0
        for i in range(len(arr)):
            if i + 1 < len(arr):
                if arr[i] != arr[i + 1]:
                    result += 1
        
        return result
    
    return smallest_change(arr)
    
    # 3rd solution
    # O(n) time | O(n) space
    # where n is the length of the input array
    def smallest_change(arr):
        # find the middle index of the array
        # for each index in the array
        # if the index is less than the middle index
        # check the next index
        # if they are not equal
        # add 1 to the result
        # return the result
        middle = len(arr) // 2
        result = 0
        for i in range(len(arr)):
            if i < middle:
                if i + 1 < len(arr):
                    if arr[i] != arr[i + 1]:
                        result += 1
        
        return result
    
    return smallest_change(arr)
    
    # 4th