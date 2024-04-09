def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    return sorted(arr, key=lambda x: (-bin(x).count('1'), x))


def sort_array_in_place(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (
                bin(arr[i]).count('1') == bin(arr[j]).count('1')
                and arr[i] > arr[j]
            ):
                arr[i], arr[j] = arr[j], arr[i]
            elif (
                bin(arr[i]).count('1') > bin(arr[j]).count('1')
                and bin(arr[i]).count('1') == bin(arr[j]).count('1')
            ):
                arr[i], arr[j] = arr[j], arr[i]
    return arr
