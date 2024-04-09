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
    # Initialization
    # max_arr: list[int] = []
    # max_num: float = -float('inf')

    # for num in arr:
    #     # print(f'[DEBUG] num: {num}')
    #     if num > max_num:
    #         max_num = num

    # for _ in range(k):
    #     max_arr.append(max_num)
    #     for num in arr:
    #         if num > max_num:
    #             max_num = num

    # return max_arr

    # Optimized
    return sorted(arr, reverse=True)[:k]


if __name__ == "__main__":
    arr = [-3, -4, 5]
    k = 3
    assert maximum(arr, k) == [-4, -3, 5]

    arr = [4, -4, 4]
    k = 2
    assert maximum(arr, k) == [4, 4]

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    assert maximum(arr, k) == [2]
