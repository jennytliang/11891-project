def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    
	Do not include these tokens in the code: reverse = False
	"""
    """
    Time complexity: O(n)
    """
    sorted_arr = sorted(array)
    reversed = sum(sorted_arr[0]) % 2 == 0 # decide which to reverse
    
    result = []
    
    if reversed:
        result = sorted_arr[::-1]

    result += sorted_arr
    return result


def partition(items, low, high):
    mid = (low + high) // 2
    pivot = items[mid][1]

    while low <= high:
        while items[low][1] < pivot:
            low += 1
        while items[high][1] > pivot:
            high -= 1
        if low <= high:
            items[low], items[high] = items[high], items[low]
            low += 1
            high -= 1

    if high > low:
        return partition(items, low, high)
    else:
        return low

def qsort(items, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    if low > high:
        return
    pivot = partition(items, low, high)
    qsort(items, low, pivot - 1)
    qsort(items, pivot + 1, high)
    return items


def _find_kth_largest(arr, k):
    """
    Fails due to:
    * stack overflow for large k(s)
    :param arr: list of tuples of (value, index)
    :param k: int
    :return: largest element or its index
    """
    for i in arr:
        for j in arr:
            if i[1] > j[1]:
                i.append(1)
            else:
                i.append(0)

        if len(max(i)) < k:
            return 0

        arr = arr[::-1]

    sorted_arr = qsort(arr)[::-1]
    print(