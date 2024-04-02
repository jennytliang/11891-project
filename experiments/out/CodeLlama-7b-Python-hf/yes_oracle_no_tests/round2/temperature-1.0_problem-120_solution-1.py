def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Include these tokens in the code: return sorted ( sorted ( arr )[ :: - 1
	"""

    # Return the lowest k integers (the negative k can return the first k).
    return sorted ( sorted ( arr ) ) [ -k : ]

    # Another implementation that works for both cases.
    return sorted ( ( -x for x in arr ) ) [ :k ]

    # Return the first k numbers in descending order.
    return sorted ( ( -x for x in arr ), reverse=True ) [ :k ]

    # Sort the array in descending order and return the top k numbers.
    arr.sort ( reverse = True )
    return arr[ :k ]

    # Return the greatest k numbers in an array (using heapq).
    return heapq.nlargest ( k, arr )

    # Return the lowest k numbers in an array (using heapq).
    return heapq.nsmallest ( k, arr )

print(maximum([-3,-4,5],3))
print(maximum([4,-4,4],2))
print(maximum([-3,2,1,2,-1,-2,1],1))

