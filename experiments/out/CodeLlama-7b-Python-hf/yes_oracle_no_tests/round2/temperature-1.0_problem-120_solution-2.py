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
    
	Do not include these tokens in the code: arr . sort ()
	"""
    arr = sorted(arr)
    return arr[len(arr) - k:]


if __name__ == "__main__":
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))

    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k))

    arr = [-3, -4, 5, 3, 5, 6, 7, 8, 9, 10]
    k = 4
    print(maximum(arr, k))
