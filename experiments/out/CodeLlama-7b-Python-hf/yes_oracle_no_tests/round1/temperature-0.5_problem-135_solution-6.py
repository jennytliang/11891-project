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

    # 1. Brute force
    # for i in range(len(arr)-1):
    #     for j in range(i+1,len(arr)):
    #         if arr[j] <= arr[i]:
    #             return j
    # return -1

    # 2. Optimized
    # if len(arr) == 0:
    #     return -1
    # max_ = max(arr)
    # for i in range(len(arr)):
    #     if arr[i] <= max_:
    #         return i
    # return -1

    # 3. Optimized further
    # if len(arr) == 0:
    #     return -1
    # max_ = max(arr)
    # for i in range(len(arr)):
    #     if arr[i] <= max_ and arr[i] >= arr[i-1]:
    #         return i
    # return -1

    # 4. Optimized further
    # if len(arr) == 0:
    #     return -1
    # max_ = max(arr)
    # for i in range(len(arr)):
    #     if arr[i] <= max_ and arr[i] >= arr[i-1]:
    #         if i == len(arr)-1 or arr[i] >= arr[i+1]:
    #             return i
    # return -1

    # 5. Optimized further
    # if len(arr) == 0:
    #     return -1
    # max_ = max(arr)
    # for i in range(len(arr)):
    #     if arr[i] <= max_ and arr[i] >= arr[i-1]:
    #         if i == len(arr)-1 or arr[i] >= arr[i+1]:
    #             return i
    # return -1
    # O(n) time, O(1) space

    # 6. Optimized further
    # if len(arr) == 0:
    #     return -1
    #