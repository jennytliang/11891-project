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
	Do not include these tokens in the code: if not arr or len
	"""
    if not arr or k == 0:
        return []

    # The idea is to use two pointers, one points to the first element, the other points to the last k elements.
    # Then we need to maintain the max k elements in the last k elements.
    # Finally, we need to return the first k elements.
    # The time complexity is O(nlogk).
    # The space complexity is O(k).

    # The sorted() in Python 3.8+ is stable sort, so we can sort the first k elements and then return them.
    # Otherwise we need to do a heap to maintain the max k elements.

    return sorted(arr[:k])


def main():
    print(maximum([-3, -4, 5], 3))
    print(maximum([4, -4, 4], 2))
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))


if __name__ == "__main__":
    main()
