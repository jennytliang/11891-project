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

    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    def get_k_max_numbers(arr, k):
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    return get_k_max_numbers(arr, k)


if __name__ == '__main__':
    arr1 = [-3, -4, 5]
    arr2 = [4, -4, 4]
    arr3 = [-3, 2, 1, 2, -1, -2, 1]
    k1 = 3
    k2 = 2
    k3 = 1
    print(maximum(arr1, k1))
    print(maximum(arr2, k2))
    print(maximum(arr3, k3))
