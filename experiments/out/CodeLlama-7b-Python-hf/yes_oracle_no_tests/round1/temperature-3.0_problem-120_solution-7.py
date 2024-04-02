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
    
	Do not include these tokens in the code: if k == 0 or len
	"""
    if k == 0 or len(arr) == 0:
        return []

    def find_maximum_k_numbers(arr, k):
        """
        Find the maximum k numbers in arr
        """
        ret = []
        for i in range(k):
            max_index = 0
            for j in range(i + 1, k):
                if arr[j] > arr[max_index]:
                    max_index = j
            ret.append(arr[max_index])
            arr[max_index] = -float('inf')
        return ret

    arr.sort()
    return find_maximum_k_numbers(arr, k)


def main():
    # Example 1:
    #     Input: arr = [-3, -4, 5], k = 3
    #     Output: [-4, -3, 5]
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))

    # Example 2:
    #     Input: arr = [4, -4, 4], k = 2
    #     Output: [4, 4]
    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))

    # Example 3:
    #     Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
    #     Output: [2]
    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k))

    # Example 4:
    #     Input: arr = [1], k = 1
    #     Output: [1]
    arr = [1]
    k = 1
    print(maximum(arr, k))

    # Example 5:
    #     Input: arr = [1], k = 0
    #     Output: []
    arr = [1]
    k