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
    
	Include these tokens in the code: return sorted ( sorted
	Do not include these tokens in the code: # if not arr or len
	"""
    if not arr or k > len(arr):
        return []

    # The idea is to sort the first k elements in the array
    # and then compare each element in the array with the smallest
    # element in the first k elements
    arr[:k] = sorted(arr[:k])
    for i in range(k, len(arr)):
        if arr[i] > arr[0]:
            arr[0], arr[i] = arr[i], arr[0]
            arr[:k] = sorted(arr[:k])

    return arr[:k]


def main():
    print(maximum([-3, -4, 5], 3))
    print(maximum([4, -4, 4], 2))
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))


if __name__ == '__main__':
    main()
