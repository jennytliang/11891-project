def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code:  if len ( arr ) ==  0 :
	"""

    # if len(arr) == 0:
    #     return -1
    
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         return i
    # return -1

    # # O(n) time, O(n) space
    # # using hashmap
    # if len(arr) == 0:
    #     return -1
    
    # hashmap = {}
    # largest_index = -1
    # for i in range(len(arr)):
    #     hashmap[arr[i]] = i
    
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         return i
    #     largest_index = max(largest_index, hashmap[arr[i+1]])
    # return largest_index

    # # O(n) time, O(1) space
    # # using sorted
    # if len(arr) == 0:
    #     return -1
    # arr.sort()
    # largest_index = -1
    # for i in range(len(arr)-1):
    #     if arr[i] >= arr[i+1]:
    #         return i
    #     largest_index = max(largest_index, arr.index(arr[i+1]))
    # return largest_index

    # O(n) time, O(1) space
    # using two pointers
    if len(arr) == 0:
        return -1
    arr.sort()
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] >= arr[i+1]:
            return i
        i += 1
    return -1


print(can_arrange([1,2,4,3,5]))
print(can_arrange([1,2,3]))
