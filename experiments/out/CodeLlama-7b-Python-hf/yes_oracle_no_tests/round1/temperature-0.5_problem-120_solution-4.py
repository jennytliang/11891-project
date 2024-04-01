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
    
	Do not include these tokens in the code:  if k ==  0 :  return
	"""

    def quick_select(arr, left, right, k):
        """
        Implementation of quick select algorithm.
        """
        if left == right:
            return arr[left]

        pivot = arr[right]
        p_index = left

        for i in range(left, right):
            if arr[i] <= pivot:
                arr[i], arr[p_index] = arr[p_index], arr[i]
                p_index += 1

        arr[p_index], arr[right] = arr[right], arr[p_index]

        if k <= p_index:
            return quick_select(arr, left, p_index - 1, k)
        if k > p_index + 1:
            return quick_select(arr, p_index + 1, right, k)
        return pivot

    return sorted(arr[:k]) if k <= len(arr) else sorted(arr)


def main():
    print(maximum([-3, -4, 5], 3))
    print(maximum([4, -4, 4], 2))
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))
    print(maximum([4, -4, 4], 3))


if __name__ == '__main__':
    main()
