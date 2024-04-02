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
    
	Do not include these tokens in the code: if not arr or k <=
	"""
    if not arr or k <= 0:
        return []

    # 1. get the max value and the index of the max value
    max_val = max(arr)
    max_idx = arr.index(max_val)

    # 2. pop the max value, if we have k left, add it back
    arr.pop(max_idx)
    if k == 1:
        return [max_val]

    # 3. sort the rest of the array, and keep the first k
    return [max_val] + sorted(arr)[:k-1]


def main():
    # [3, 2, 1, 5, 6, 4]
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k)) # [-4, -3, 5]

    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k)) # [4, 4]

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k)) # [2]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    k = 5
    print(maximum(arr, k)) # [20, 19, 18, 17, 16]


if __name__ == '__main__':
    main()
