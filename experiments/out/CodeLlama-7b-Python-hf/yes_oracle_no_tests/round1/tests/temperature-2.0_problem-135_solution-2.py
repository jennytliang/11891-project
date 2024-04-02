def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len ( arr ) -
	"""
    # 1st approach:
    # O(n) time | O(1) space
    # for i in range ( len ( arr ) - 1 ):
    #     if arr[i] >= arr[i + 1]:
    #         return i
    # return -1

    # 2nd approach:
    # O(n) time | O(1) space
    # for i in range ( len ( arr ) ):
    #     if arr[i] <= arr[i - 1]:
    #         return i - 1
    # return -1

    # 3rd approach:
    # O(n) time | O(1) space
    # for i in range ( len ( arr ) ):
    #     if arr[i] > arr[i - 1]:
    #         return i - 1
    # return -1

    # 4th approach:
    # O(n) time | O(1) space
    # for i in range ( len ( arr ) ):
    #     if arr[i] <= arr[i - 1]:
    #         return i - 1
    # return -1

    # 5th approach:
    # O(n) time | O(1) space
    # if len ( arr ) < 2:
    #     return -1
    #
    # for i in range ( 1, len ( arr ) ):
    #     if arr[i] <= arr[i - 1]:
    #         return i - 1
    #
    # return len ( arr ) - 1

    # 6th approach:
    # O(n) time | O(1) space
    # for i in range ( len ( arr ) - 1 ):
    #     if arr[i] > arr[i + 1]:
    #         return i
    # return -1

    # 7th approach:
    # O(n) time | O(1) space
    # for i in range ( len ( arr ) ):
    #     if arr[i] <= arr[i - 1]:




import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[[1, 2, 4, 3, 5]], [[1, 2, 4, 5]], [[1, 4, 2, 5, 6, 7, 8, 9, 10]], [[4, 8, 5, 7, 3]], [[]], [[1]], [[1, 2, 3, 4, 5]], [[5, 4, 3, 2, 1]], [[1, 3, 5, 4, 6, 7, 9, 8]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[1, 4, 2, 5, 6, 7, 8, 9, 10, 3]], [[1, 3, 2, 4]], [[5, 4, 3, 2]], [[-1, 0, 1, 2, 3]], [[2, 3, 1, 4]], [[1, 3, 4]], [[6, 0, 1, 2, 3]], [[1, 4, 2, 5, 6, 8, 9, 10, 3]], [[2, 3, 4, 5]], [[2]], [[1, 2, 5, 6, 8, 9, 10, 3]], [[5, 4, 3, 1, 2]], [[1, 3, 5, 4, 6, 7, 8]], [[3, 1]], [[1, 4, 2, 5, 6, 7, -1, 9, 10, 3]], [[1, 4, 2, 5, 7, -1, 9, 10, 3]], [[6, 0, 1, 3]], [[-1, 0, -2, 1, 2, 3]], [[1, 4, 2, 5, 6, 8, 7, -1, 9, 10, 3]], [[10, 1]], [[5, 4, 2]], [[2, 1]], [[3, 2, 4]], [[5, 4, 6, 2]], [[1, 4, 2, 6, 8, 7, -1, 9, 10, 3]], [[6, 0, 1, 2, 4]], [[5, 4, 2, 1, 8]], [[9, 8, 7, 6, 5, 4, 3, 2, 1]], [[8, 4, 3, 2]], [[1, 4, 2, 6, 7, 5, -1, 10, 3]], [[-1, 2, 1]], [[1, 3, 5, 4, 6, 7, 9]], [[1, 3, -2]], [[-1, 2, 0]], [[5, 10, 1]], [[6, 0, 10, 2, 4]], [[6, 3, 4, 5]], [[1, 4, 2, 5, 6, 7, -1, 9, 3]], [[6, 0, 10, 4]], [[2, 3, 7, 4]], [[10, 8, 7, 6, 5, 4, 3, 2, 1]], [[6, 0, 2, 4]], [[2, 4, 10, 5]], [[8, 4, 3]], [[3]], [[5, 4, 6, -2]], [[5, 4, 2, 1]], [[4, 2, 1]], [[10, 3, -2, -1, 1]], [[1, 3]], [[3, 7]], [[0, 4, 2, 1, 8]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 0]], [[10, 3, 2, -2, -1, 1]], [[6, 4, 3, 1, 2]], [[-1, 0, 1, 7, 3]], [[1, 8, 4, 3, 2]], [[1, 3, 5, 4, 6, 7, 10, 8]], [[3, 1, 4]], [[1, 6, -2, 3]], [[5, 4, -3]], [[-1, 0, 6, 7, 3]], [[5, -3]], [[6, 0, 1, 2, 3, 4]], [[-1, 5, 0, 1, 2, 3]], [[7]], [[1, 3, 5, 4, 10, 6, 7, 9]], [[6, 3, 2, 4]], [[1, 3, 2, -3, 4]], [[1, 4, 2, 5, -2, 7, -1, 9, 10, 3]], [[1, 3, 5, 4, -1, 6, 7, 9, 8]], [[1, 4, 5, 6, 8, 7, -1, 9, 10, 3]], [[-3, 5, 4, -2]], [[5, 3, 2]], [[-1, -2, 1, 2, 3]], [[2, 1, 4, 10, 5]], [[0, 3]], [[-2, 5, -3]], [[2, 3, 4, 7]], [[10, 9, 8, 7, 6, 5, 4, 3, 1, 0]], [[6, 1, 2, 4]], [[4, 1]], [[-1, 2]], [[5, 6, 7, 0, 10, 4]], [[0, 1, 2, 4]], [[10]], [[1, 6, 0, -2, 3]], [[5, -3, 4, 6, -2]], [[5, 10]], [[4, 2, 1, 3, 5, 6, 7]], [[10, 9, 8, 4, 7, 6, 5, 2, 1]], [[3, 6, 9, 12, 15, 18, 21, 19, 16, 13, 10, 7, 4, 1, 2, 5, 8, 11, 14, 17, 20]], [[1, 3, 5, 4, 2, 6, 8, 7, 10]], [[1, 2, 3, 10, 9, 8, 7, 6, 5]], [[10, 9, 8, 1, 2, 3, 4, 7, 6, 5]], [[1, 10, 2, 9, 3, 8, 4, 7, 5, 6]], [[5, 4, 3, 2, 1, 6, 7, 8, 9, 10]], [[1, 3, 2, 5, 4, 7, 6, 9, 8, 10]], [[4, 3, 2, 1]], [[4, 8, 2, 1]], [[4, 6, 2, 1]], [[10, 8, 17, 7, 6, 5, 2, 18, 1]], [[3, 6, 9, 12, 15, 18, 21, 19, 16, 13, 10, 7, 4, 1, 2, 5, 8, 14, 17, 20]], [[10, 9, 8, 4, 17, 6, 5, 2, 1]], [[1, 3, 2, 5, 4, 7, 9, 8, 10]], [[4, 6, 3, 1]], [[4, 3, 2, 5, 1]], [[1, 2, 4, 10, 9, 8, 7, 6, 5]], [[2, 4, 10, 9, 8, 7, 6, 5]], [[1, 5, 4, 2, 6, 8, 7, 10]], [[1, 3, 5, 4, 2, 8, 7, 10]], [[10, 9, 8, 1, 2, 3, 4, 7, 6]], [[4, 3, 12, 2, 1]], [[19, 4, 3, 2, 1]], [[10, 9, 8, 4, 18, 6, 5, 2, 1]], [[4, 2]], [[4, 3, 2, 5]], [[4, 9, 3, 2, 5]], [[4, 2, 5, 1]], [[4, 3]], [[4, 6, 3]], [[10, 9, 8, 1, 18, 2, 3, 4, 7, 6]], [[9, 4, 2, 1]], [[4, 3, 1]], [[0, 1, 3, 2, 5, 4, 7, 9, 8, 10]], [[0, 1, 3, 2, 5, 4, 6, 7, 9, 8, 10]], [[3, 2, 1, 5]], [[1, 3, 5, 4, 0, 2, 6, 8, 7, 10]], [[0, 3, 12, 18, 2, 5, 4, 6, 7, 9, 8, 10]], [[1, 3, 5, 2, 6, 8, 7, 10]], [[4]], [[1, 3, 5, 2, 6, 8, 10]], [[1, 4, 5, 2, 6, 8, 10]], [[1, 2, 3, 10, 9, 8, 6, 5]], [[4, 3, 2, 5, 16, 1]], [[1, 3, 2, 5, 4, 7, 6, 8, 10]], [[1, 5, 4, 2, 8, 7, 10]], [[4, 3, 2, 5, 19, 1]], [[1, 0, 3, 2, 5, 4, 7, 6, 9, 8]], [[4, 2, 3, 5, 1]], [[0, 3, 12, 18, 21, 5, 4, 6, 7, 9, 11, 8, 10]], [[5, 4, 9]], [[1, 0, 5, 4, 2, 6, 8, 7, 10]], [[0, 1, 3, 5, 4, 6, 7, 9, 8, 10]], [[19, 4, 2, 1]], [[19, 4, 17, 2, 1]], [[11, 3]], [[1, 3, 5, 4, 0, 16, 6, 8, 7, 10]], [[8, 3, 1]], [[5, 15, 2]], [[11, 2, 3]], [[1, 2, 4, 10, 9, 7, 6, 5]], [[3, 5]], [[3, 6, 9, 12, 15, 18, 21, 19, 16, 13, 7, 4, 1, 2, 5, 8, 14, 17, 20]], [[19, 4, 3, 10, 8, 9, 1]], [[1, 3, 5, 4, 0, 16, 8, 7, 10]], [[19, 0, 4, 2, 1]], [[9, 13, 4, 2, 1]], [[2, 5]], [[4, 16, 2, 5, 19, 1]], [[5, 4, 9, 2]], [[10, 9, 8, 4, 17, 6, 5, 15, 2, 1]], [[3, 6, 9, 12, 15, 18, 21, 19, 16, 13, 4, 1, 2, 5, 8, 14, 17, 20]], [[19, 4, 12, 2, 1]], [[5]], [[8, 14, 3, 1]], [[1, 3, 2, 5, 14, 4, 0, 16, 7, 10]], [[19, 4, 12, 2]], [[3, 5, 4, 8, 15, 7, 10]], [[5, 2]], [[1, 4, 5, 18, 2, 6, 8, 10]], [[1, 4, 5, 2, 6, 8]], [[2, 1, 5]], [[3, 6, 9, 12, 15, 21, 19, 16, 13, 10, 7, 4, 1, 2, 5, 8, 11, 14, 17, 20]], [[10, 9, 8, 1, 2, 3, 4, 7, 5]], [[9, 4, 2]], [[4, 18, 3, 1]], [[15, 2, 3, 10, 9, 8, 6, 5]], [[9, 2, 1]], [[4, 2, 5, 19, 1]], [[4, 6, 17]], [[1, 3, 5, 2, 4, 8, 10]], [[5, 4, 2, 6, 8, 7, 10]], [[8, 4, 15, 9, 2]], [[1, 5, 0, 16, 8, 7, 10]], [[5, 4]], [[5, 4, 3, 2, 1, 6, 7, 9, 10]], [[4, 3, 5, 16, 1]], [[3, 4]], [[8, 4, 3, 15, 9, 2]], [[4, 3, 7, 5, 19, 1]], [[4, 6, 2, 7, 9]], [[6, 9, 12, 15, 21, 19, 16, 13, 10, 7, 4, 1, 2, 5, 8, 11, 14, 17, 20]], [[5, 15]], [[4, 21, 3, 9]], [[11, 2]], [[1, 3, 5, 2, 6, 8]], [[1, 0, 5, 14, 2, 6, 8, 7, 10]], [[6, 2, 1]], [[5, 4, 15, 2]], [[20, 19, 4, 3, 2, 1]], [[1, 3, 2, 6, 8, 7, 10]], [[5, 4, 3, 1, 6, 7, 9, 10]], [[12, 3]], [[8, 4, 15, 10, 9, 2]], [[1, 3, 5, 4, 0, 17, 16, 8, 7, 10]], [[3, 5, 0, 16, 8, 7, 10]], [[19, 18, 3, 1]], [[5, 9]], [[4, 5, 1]], [[15]], [[3, 2, 1]], [[0, 20, 2, 1]], [[15, 1, 12, 3, 5, 4, 2, 8, 7, 10]], [[1, 3, 2, 6, 5, 8]], [[1, 3, 5, 9, 6, 8, 10]], [[2, 3]], [[3, 4, 21, 2, 9]], [[4, 10, 2, 7]], [[12, 1]], [[20, 1, 2, 3, 10, 9, 8, 7, 6, 5]], [[3, 2, 5]], [[4, 0, 1]], [[0, 1, 5, 4, 6, 7, 9, 8, 10]], [[1, 10, 2, 9, 3, 8, 4, 13, 5, 6]], [[1, 3, 5, 2, 21, 4, 8, 10]], [[2, 4, 10, 8, 7, 6, 5]], [[8, 4, 15, 9]], [[3, 12, 2, 1]], [[3, 5, 0, 16, 15, 8, 7]], [[19, 4, 13, 2, 1]], [[15, 3, 5, 4, 2, 8, 7, 10]], [[1, 3, 5, 6, 8, 14, 10]], [[19, 3, 0, 4, 2, 1]], [[19, 4, 12, 1]], [[4, 5, 19, 1]], [[10, 8, 17, 7, 5, 3, 18, 1]], [[3, 6, 9, 12, 15, 18, 21, 19, 16, 13, 4, 1, 2, 8, 14, 17, 20]], [[11, 10, 2]], [[4, 9, 3, 2]], [[2, 8, 4, 3, 15, 9]], [[19, 3, 13, 2, 1]], [[12, 5, 9]], [[1, 3, 2, 5, 14, 4, 16, 7, 10]], [[10, 2, 7]], [[4, 3, 2, 1, 6, 7, 8, 9, 10]], [[1, 20, 5, 2, 21, 4, 8, 10]], [[5, 19, 1]], [[1, 3, 5, 4, 2, 8, 10]], [[1, 3, 2, 12, 8, 7, 10]], [[13, 6, 2, 1]], [[19, 4, 12, 0, 1]], [[10, 3, 5, 19, 1]], [[5, 6, 9]], [[19, 8, 14, 3]], [[4, 18, 20, 5, 2, 1]], [[15, 1, 12, 20, 5, 4, 2, 8, 7, 10]], [[10, 9, 21, 4, 17, 6, 15, 2, 1]], [[15, 5, 4, 2, 7, 10]], [[4, 5, 12, 1]], [[1, 4, 5, 2, 11, 8, 10, 6]], [[-1, 5, 0, 2]], [[16, 9, 2, 1]], [[2, 3, 10, 9, 8, 6, 1, 5]], [[4, 6, 2, 0, 1]], [[20, 4, 12, 1]], [[3, 2, 5, 19, 1]], [[1, 3, 0, 6, 8, 14, 10]], [[4, 15, 2]], [[4, 10, 12]], [[9]], [[3, 2, 5, 4, 7, 9, 8, 10]], [[4, 18, 20, 5, 9, 1]], [[4, 16, 2, 5, 19]], [[5, 4, 3, 2, 1, 6, 15, 9, 10]], [[4, 5, 2, 6, 8]], [[4, 20, 5, 9, 1]], [[15, 16, 2, 3, 5, 19]], [[10, 9, 8, 1, 5, 2, 3, 4, 7, 6]], [[3, 2, 15, 5]], [[10, 8, 17, 7, 6, 2, 18, 1]], [[1, 2, 4, 17, 10, 9, 7, 6, 18]], [[1, 3, 2, 5, 8]], [[3, 2]], [[4, 10, 7]], [[18, 4, 6, 17]], [[19, 4, 3, 20, 2]], [[5, 6, 4, 9]], [[1, 3, 5, 4, 6, 7, 9, 8, 10]], [[1, 20, 5, 6, 2, 21, 4, 8, 10]], [[19, 4, 14, 3, 2, 1]], [[19, 18, 1]], [[4, 3, 2, 0, 5, 16, 1]], [[19, 4, 10, 8, 9, 1]], [[19, 5]], [[3, 0, 2, 1]], [[4, 13, 12]], [[37.45846213316932, -21.8131802318007, -18.630055685163583, -76.49298700358514, -63.655488885630994, 81.75342869524977, 96.86306070463999, 77.21191831561089, 22.028951203200748, -54.83341431889768]], [[20, 6, 3, 2, 1]], [[1, 20, 3, 5, 4, 0, 2, 6, 8, 7, 10]], [[6, 4, 3, 2, 1]], [[5, 2, 6, 21, 8]], [[1, 2, 10, 9, 8, 6, 5, 3]], [[1, 3, 2, 5, 14, 4, 0, 16, 10]], [[19, 4, 10, 7, 9]], [[1, 3, 2, 5]], [[3, 6, 9, 12, 0, -1, 21, 19, 16, 13, 10, 7, 4, 1, 2, 5, 8, 11, 14, 17, 20]], [[5, 3, 2, 1, 6, 7, 8, 9, 10]], [[2, 0]], [[4, 2, 10, 9, 8, 6, 5, 3]], [[3, 5, 0, 16, 15, 7]], [[19, 4, 13, 2, 8]], [[4, 3, 2, 1, 6, 15, 9, 10]], [[5, 4, 3, 2, 1, 6, 7, 17, 10]], [[15, 2, 5, 19]], [[18, 9, 6, 15, 16, 2, 3, 5, 19]], [[1, 3, 2, 6, 8]], [[19, 12, 1]], [[-1, 12, 3]], [[22.028951203200748, -21.8131802318007, 37.45846213316932, -76.49298700358514, 90.03562713717855]], [[6, 21, 1]], [[6]], [[15, 16, 2, 3, 4, 19]], [[9, 1]], [[1, 10, 2, 9, 3, 18, 8, 4, 5, 6]], [[4, 18, 20, 2, 1]], [[1, 4, 2]], [[1, 5, 2, 6, 8]], [[18, 5]], [[20, 15]], [[4, 10, 11, 12]], [[3, 2, 12, 8, 7, 10]], [[20]], [[8]], [[10, 3, 16, 19, 1]], [[13, 1]], [[19, 4, 3, 20, 1]], [[19, 4, 6, 2, 1]], [[0, 5, 4]], [[8, 3]], [[17, 3, 0, 2]], [[20, 5, 1, 2]], [[10, 9, 8, 5, 2, 3, 4, 7, 6]], [[7, 4, 15, 9]], [[19, 4, 10, 8, 9, 16, 1]], [[19, 4, 13, 3, 2, 1]], [[10, 9, 1, 2, 3, 4, 7, 6, 5]], [[4, 3, 5, 1]], [[0, 20, 1, 5, 4, 6, 7, 9, 8, 10]], [[1, 5, 4, 2, 6, 7, 10]], [[19, 4, 3, 8, 9, 1]], [[1, 5]], [[13, 9, 0, 8, 4, 18, 6, 5, 2, 1]], [[4, 2, 1, 6, 15, 9, 10]], [[4, 9, 19, 2]], [[4, 3, 2, 5, 21]], [[10, 3, 6, 19, 1]], [[4, 17, 18, 20, 2, 1]], [[20, 3, 12, 1]], [[5, 1]], [[2, 11, 3]], [[1, 0, 3]], [[10, 9, 21, 17, 6, 15, 2, 1]], [[19, 4, 6, 2]], [[4, 1, 3, 5]], [[2, 3, 1]], [[0, 1, 3, 2, 5, 4, 6, 15, 7, 9, 8, 10]], [[4, 2, 13, 6, 15, 9, 10]], [[4, 3, 2, 6]], [[1, 3, 0, 5, 4, 2, 6, 8, 7, 10]], [[10, 2]], [[2, 21, 5]], [[4, 3, 0, 5, 16, 1]], [[1, 4, 20, 2, 6, 8, 10]], [[10, 8, 17, 6, 2, 18]], [[1, 10, 9, 3, 8, 4, 13, 5, 6]], [[5, 2, 1, 4, 21, 8]], [[1, 3, 5, 4, 6, 7, 8, 10]], [[6, 3]], [[1, 5, 2, 6]], [[1, 4, 15, 18, 2, 6, 8, 10]], [[9, 2]], [[8, 4, 3, 15, 9]], [[18, 9, 6, 15, 20, 16, 2, 3, 5, 19]], [[19, 21, 17, 3, 1]], [[-1, 15]], [[4, 2, 10, 9, 8, 6, 13, 5, 3]], [[4, 3, 11, 2, 5, 21]], [[1, 3, 2, 5, 4, 7, 6, 9, 10]], [[6, 16, 1]], [[9, 8, 5, 2, 3, 4, 7, 6]], [[20, 1, 2, 3, 10, 9, 8, 7, 17, 5]], [[5, 10, 7]], [[19, 5, 17, 7, 2, 1]], [[19, 4, 18, 3, 1]], [[8, 4, 13, 9]], [[11, 4, 10, 9, 12]], [[19, 4, 12, 15, 2]], [[4, 2, 3, 5, 0]], [[1, 15, 3]], [[1, 3, 4, 2, 6, 8, 7, 10]], [[18, 9, 4, 6, 15, 20, 16, 2, 3, 5, 19]], [[10, 3, 12, 6, 19, 1]], [[3, 2, 5, 4, 7, 8, 10]], [[3, 2, 5, 4, 14, 7, 8, 10]], [[1, 13, 4, 5, 18, 2, 6, 8, 10]], [[15, 1, 12, 3, 19, 4, 2, 8, 7, 10]], [[18, 4, 5]], [[1, 3, 2, 5, 13, 4, 7, 6, 9, 8, 10]], [[4, 1, 3, 11, 2, 5, 21]], [[4, 19, 2, 5, 1]], [[19, 4, 13, 3, 2]], [[4, 9, 19, 3]], [[1, 5, 2, 6, 20]], [[5, 3, 2, 1]], [[19, 4, 10, 8, 9, 18, 16, 1]], [[4, 18, 2, 1]], [[1, 4, 15, 18, 11, 2, 6, 8, 10]], [[8, 4, 15, 2]], [[20, 19, 4, 3, 1, 0]], [[4, 2, 13, 12, 15, 9, 10]], [[1, 5, 6, 8, 14, 10]], [[16, 4, 12, 2]], [[5, 15, 17, 2]], [[1, 4, 15, 18, 11, 2, 8, 10]], [[19, 4, 13, 2]], [[1, 3, 4, 0, 2, 8, 7, 10]], [[3, 2, 5, 7, 9, 8, 10]], [[19, 4, 10, 8, 9, 16]], [[1, 20, 5, 2, 3, 21, 4, 8, 10]], [[6, 20, 1]], [[8, 10, 12]], [[3, 2, 4, 5, 21]], [[1, 20, 5, 16, 3, 4, 8, 10]], [[11, 4, 17, 18, 20, 2, 1]], [[11, 2, 4]], [[4, 6]], [[13, 4, 10, 12]], [[18, 19, 3, 13, 2, 1]], [[8, 4, 2]], [[10, 8, 17, 7, 9, 6, 2, 18, 1]], [[20, 1, 2, 3, 10, 9, 8, 6, 5]], [[0, 1, 5, 6, 4, 8, 14, 10]], [[4, 2, 3, 1]], [[3, 5, 0, 16, 7, 10]], [[14, 5, 2, 19, 1]], [[1, 3, 9, 6, 8, 10]], [[5, 2, 6, 20]], [[12, 2, 3]], [[8, 4, -1, 3, 15, 9, 2]], [[1, 0, 2, 5, 4, 7, 6, 9, 8]], [[1, 5, 0, 16, 8, 7, 12, 10]], [[13, 10, 12]], [[2, 4]], [[15, 1, 12, -1, 20, 5, 4, 2, 8, 7, 10]], [[20, 2, 3, 10, 9, 8, 7, 17, 5]], [[4, 6, 3, 2, 5, 1]], [[10, 2, 12, 6, 1]], [[3, 10, 2, 7]], [[5, 9, 19, 3]], [[1, 5, 4, 2]], [[3, 5, 2, 16, 8, 7, 10]], [[4, 20, 1]], [[19, 17, 4, 3, 21, 2]], [[3, 5, 18, 0, 16, 15, 8, 7]], [[4, 6, 2, 5, 1]], [[13, 4, 2, 1]], [[9, 6]], [[20, 1, 2, 4, 10, 9, 8, 6, 5]], [[1, 3, 5, 16, 4, 2, 8, 7, 10]], [[8, 4, 1]], [[4, 3, 1, 5]], [[8, 7, 4, 15, 9]], [[20, 4, 6, 3]], [[10, 8, 5, 2, 3, 4, 7, 6]], [[1, 5, 4, 2, 6, 8, 10]], [[10, 21, 17, 15, 2]], [[8, 4, 15, 11, 9]], [[19, 13, 3, 2, 1]], [[0, 5]], [[13, 11, 4, 10, 12]], [[20, 5, 1]], [[5, 4, 21, 9]], [[3, 2, 4, 7, 9, 8, 10]], [[1, 3, 5, 4, 0, 6, 8, 7, 10]], [[4, 5, 6, 1]], [[16, 15]], [[0, 2, 3, 10, 9, 8, 6, 1, 5]], [[13, 12]], [[15, 2, 3, 10, 9, 6, 5]], [[13]], [[4, 17, 18, 20, 1]], [[10, 16, 17, 7, 5, 3, 18, 1]], [[3, 6, 9, 12, 15, -1, 21, 19, 16, 13, 10, 7, 4, 1, 2, 5, 8, 11, 14, 17, 20]], [[16, 9, 3, 1]], [[20, 4, 17, 2, 1]], [[19, 4, 3, 12, 2]], [[13, 11, 4, 10, 14]], [[20, 3, 0, 4, 2, 1]], [[21, 1]], [[19, 4, 3, 1]], [[16, 4, 12, 3]], [[19, 4, 10, 8, 9, 11, 1]], [[4, 18, 20, 5, 1]], [[1, 5, 4, 2, 6, 8]], [[1, 3, 6, 8, 7, 10]], [[3, 0, 6, 8, 14, 10]], [[19, 6, 5]], [[1, 4, 16, 15, 18, 11, 6, 8, 10]], [[8, 15]], [[15, 2, 3, 9, 6, 5]], [[4, 8, 19, 16, 3]], [[4, 18, 20, 5, 2]], [[19, 4, 10, 8, 11, 1]], [[12]], [[9, 7, 8, 20, 1]], [[16, 1]], [[1, 10, 2, 9, 3, 18, 8, 4, 13, 6]], [[16, 21, 1]], [[19, 20, 13, 4, 10, 8, 9, 16]], [[1, 5, 0, 16, 7, 10]], [[15, 2, 3, 9, 8, 6, 5]], [[7, 4, 3, 15, 9]], [[2, 12]], [[4, 11, 7]], [[5, 4, 17, 2, 1]], [[6, 2, 5, 1]], [[8, 4, 10, 9, 2]], [[6, 12, 2, 3]], [[4, 10, 20, 12]], [[3, 2, 12, 8, 7, 14, 10]], [[1, 3, 14, 5, 4, 0, 17, 15, 16, 10]], [[4, 1, 16, 5]], [[4, 10, 14, 12]], [[1, 0, 5, 4, 10, 7, 6, 9, 8]], [[1, 4, 15, 11, 2, 8, 10]], [[19, 17, 4, 3, 21, 20, 2]], [[10, 11]], [[1, 5, 4, 6, 8, 7, 10]], [[1, 4, 11, 2, 5, 8]], [[0, 7, 1, 5, 6, 4, 8, 14, 10]], [[19, 4, 10, 8, 11, -1]], [[5, 4, 15, 17, 2]], [[16, 9, 3, 2, 1]], [[20, 19, 4, 12, 2, 1]], [[4, 14, 2]], [[7, 15]], [[1, 5, 6, 8]], [[1, 3, 2, 0, 13, 4, 7, 6, 9, 8, 10]], [[15, 16, 2, 7, 3, 5, 19]], [[17, 5, 9, 19, 3]], [[10, 20, 2, 7]], [[18, 3]], [[16, 0, 6, 8, 14]], [[1, 3, 2, 8]], [[1, 3, 2, 5, 14, 4, 16, 10]], [[15, 8, 2, 7, 3, 10]], [[4, 9, 3, 11, 2, 5, 21]], [[1, 10, 2, 9, 3, 18, 8, 4, 6]], [[1, 13, 4, 5, 18, 2, 6, 8, 11]], [[1, 5, 0, 17, 8, 10]], [[8, 20, 19, 4, 3, 2, 1]], [[5, 4, 3, 1, 6, 8, 9, 10]], [[4, 0, 3, 12, 2, 19, 1]], [[1, 3, 4, 2, 6, 8, 7, 9]], [[5, 10, 14, 12]], [[11, 1, 4]], [[1, 20, 6, 2, 21, 8, 10]], [[4, 13]], [[3, -1, 0, 2, -2]], [[1, 2, 3, 4, 5, 6]], [[6, 5, 4, 3, 2, 1]], [[1, 5, 2, 4, 3]], [[4, 2, 1, 3, 11, 7]], [[6, 1, 3, 11, 7]], [[3, 6, 9, 12, 15, 18, 21, 19, 13, 10, 7, 4, 1, 2, 5, 8, 11, 14, 17, 20]], [[1, 2, 3, 10, 9, 8, 7, 5]], [[1, 3, 7]], [[2, 1, 3, 11, 7]], [[0, 2, 3, 10, 9, 8, 6, 5]], [[1, 2, 3, 18, 9, 8, 7, 5]], [[1, 10, 2, 9, 3, 14, 4, 7, 5, 6]], [[1, 2, 4, 18, 9, 8, 7, 5]], [[0, 1, 3, 7]], [[2, 1, 3, 7]], [[10, 9, 8, 1, 2, 4, 7, 6, 5]], [[0, 2, 3, 21, 9, 8, 6]], [[0, 2, 4, 10, 9, 8, 6, 5]], [[1, 10, 2, 9, 14, 7, 5, 6]], [[19, 2, 1, 3, 11, 7]], [[1, 2, 18, 9, 8, 7]], [[2, 3, 11, 7]], [[2, 3, 10, 9, 8, 7, 6, 5]], [[1, 2, 3, 10, 9, 7, 5]], [[18, 1, 3]], [[2, 3, 10, 9, 7, 5]], [[1, 2, 3, 18, 9, 8, 7]], [[0, 2, 4, 10, 17, 9, 8, 6, 5]], [[5, 4, 3, 2, 12]], [[18, 1, 20, 3]], [[1, 2, 18, 9, 8, 7, 5]], [[2, 3, 10, 9, 8, 7, 6]], [[1, 2, 18, 10, 7, 5]], [[16, 2, 3, 10, 9, 8, 7, 6, 5]], [[16, 2, 3, 10, 9, 8, 6]], [[5, 14, 3, 2, 12]], [[1, 14, 3, 18, 9, 8, 7, 5]], [[13, 1, 2, 3, 10, 9, 8, 7, 5]], [[4, 2, 1, 19, 5, 6, 7]], [[4, 2, 1, 6, 7, 8, 9, 10]], [[5, 4, 3, 2, 10, 12]], [[4, 2, 3, 1, 19, 5, 6, 7]], [[2, 10, 9, 7, 5]], [[1, 4, 7]], [[4, 3, 2, 1, 6, 8, 9, 10, 7]], [[1, 2, 18, 9, 8, 7, 11]], [[14, 4, 7]], [[1, 3, 10, 9, 8, 7, 5]], [[2, 1, 3, 10, 7]], [[10, 9, 8, 2, 4, 7, 6, 5]], [[1, 3, 0, 10, 9, 8, 6, 15]], [[3, 6, 9, 12, 15, 18, 21, 19, 13, 10, 7, 4, 1, 2, 5, 8, 14, 17, 20]], [[2, 3, 10, 9, 7, 6]], [[18, 1, 21, 20, 3]], [[1, 2, 18, 10, 7, 4]], [[2, 1, 6, 7, 9, 10]], [[11, 2, 18, 10, 7, 4]], [[1, 2, 5, 4, 7, 6, 9, 8, 10]], [[18, 1, 3, 2]], [[2, 3, 10, 9, 8, 6, 5]], [[3, 5, 4, 2, 6, 8, 7, 10]], [[5, 14, 3, 2, 6, 12]], [[2, 1, 3, 11]], [[4, 2, 1, 5, 7, 8, 9, 10]], [[4, 2, 1, 6, 7, 8, 9, 20, 10]], [[4, 2, 1, 5, 7, 9, 10]], [[2, 3, 10, 9, 14, 8, 6, 5]], [[4, 2, 1, 6, 7, 11, 9]], [[1, 2, 4, 18, 9, 3, 13, 7, 5]], [[3, 2, 5, 4, 7, 6, 9, 8, 10]], [[5, 14, 3, 12]], [[19, 2, 0, 3, 11, 7]], [[2, 1, 4, 7]], [[2, 17, 3, 10, 9, 8, 6, 5]], [[2, 17, 11, 3, 10, 9, 8, 6, 5]], [[11, 1, 18, 10, 7, 4]], [[4, 2, 1, 19, 5, 14, 6, 7]], [[4, 3, 2, 1, 6, 7, 8, 11, 10]], [[1, 3, 10, 9, 8, 7]], [[1, 7]], [[4, 2, 19, 5, 6, 7]], [[6, 1, 3, 11, 13]], [[2, 1, 5, 7, 9, 10]], [[16, 2, 3, 11, 7]], [[2, 17, 11, 3, 10, 9, 8, 6]], [[4, 2, 1, 17, 19, 5, 14, 6, 7]], [[1, 2, 8, 3, 10, 9, 7, 5]], [[6, 1, 13]], [[2, 3, 10, 9, 7]], [[11, 3, 10, 9, 7, 5]], [[3, 4, 7]], [[1, 2, 18, 9, 8, 19]], [[12, 1, 10, 2, 9, 3, 14, 4, 7, 5, 6]], [[4, 2, 1, 5, 7, 8, 9]], [[4, 2, 5, 6, 7]], [[2, 4, 7]], [[2, 1, 6, 7, 8, 9, 10]], [[2, 11, 7]], [[1, 10, 2, 9, 3, 8, 7, 5, 6]], [[2, 10, 9, 7]], [[13, 1, 2, 3, 6, 10, 9, 8, 7, 5]], [[2, 3, 10, 5, 8, 7, 6]], [[1, 3, 2]], [[11, 5, 4, 3, 2, 10, 12]], [[0, 2, 4, 10, 17, 9, 8, 5]], [[16, 2, 10, 9, 8, 7, 6, 5]], [[11, 3, 10, 9, 8, 7, 5]], [[1, 4, 3, 7]], [[2, 1, 3, 11, 18]], [[4, 2, 1, 19, 5, 14, 18, 7]], [[2, 17, 4, 7]], [[2, 1, 5, 7, 10]], [[4, 3, 2, 1, 6, 7, 8, 9, 20, 10]], [[14, 1, 3, 7]], [[4, 2, 1, 12, 6, 7, 11, 9]], [[6, 1, 3, 12, 11, 13]], [[2, 18, 10, 6, 4]], [[6, 4, 3, 2, 12]], [[0, 2, 10, 9, 8, 6, 5]], [[4, 2, 1, 5, 7, 9, 10, 3]], [[2, 20, 10, 9, 7]], [[1, 2, 4, 20, 18, 9, 8, 7, 5]], [[13, 1, 2, 3, 10, 9, 8, 7]], [[4, 2, 1, 21, 6, 7, 8, 9, 10]], [[2, 17, 11, 3, 10, 9, 8, 13, 6, 5]], [[18, 1, 21, 3]], [[2, 10, 9, 7, 3, 5]], [[4, 2, 1, 6, 8, 9, 10]], [[4, 3, 2, 1, 6, 7, 8, 9]], [[4, 2, 1, 6, 8, 19, 9, 10]], [[3, 5, 4, 2, 6, 8, 20, 10]], [[4, 17, 1, 5, 7, 8, 9, 10]], [[0, 1, 2, 3, 7]], [[18, 1, 20, 15]], [[4, 2, 1, 5, 7, 14, 8, 9, 10]], [[2, 1, 5, 3, 10, 7]], [[2, 7]], [[18, 1, 14, 3]], [[1, 3, 0]], [[1, 0, 2, 10, 9, 8, 6, 5]], [[10, 0, 7]], [[1, 2, 9, 14, 7, 5, 6]], [[2, 20, 10, 9, 8, 7, 6]], [[1, 5, 4, 2, 6, 12, 7, 10]], [[1, 2, 18, 9, 3, 8, 7, 5]], [[3, 10, 8, 9, 6, 5]], [[4, 7]], [[4, 14]], [[2, 4, 10, 9, 7, 5]], [[2, 0, 5, 3, 10, 7]], [[1, 2, 3, 18, 8, 7]], [[1, 18, 9, 8, 7]], [[6, 20, 10, 9, 7]], [[1, 2, 9, 14, 7, 5, 10, 6]], [[2, 1, 3, 13]], [[2, 10, 9, 7, 6, 5]], [[2, 1, 3, 10, 11, 18]], [[9, 14, 4, 7]], [[1, 2, 17, 3, 18, 9, 8, 7, 5]], [[18, 3, 2]], [[0, 2, 4, 10, 17, 9, 6, 5]], [[3, 2, 18, 10, 6, 4]], [[18, 1, 15]], [[0, 14, 3, 18, 9, 8, 7, 5]], [[4, 2, 1, 6, 8, 13, 19, 9, 10]], [[1, 14, 17, 4, 7]], [[1, 15, 2, 9, 14, 7, 5, 6]], [[13, 11, 3, 6, 10, 9, 8, 7, 5]], [[4, 16, 2, 1, 6, 8, 13, 19, 9, 10]], [[1, 11, 3, 2]], [[3, 1, 6, 8, 9, 10]], [[1, 2, 9, 8, 19]], [[17, 18, 1, 21, 3]], [[13, 1, 2, 3, 10, 9, 7, 5]], [[3, 5, 2, 6, 8, 20, 10]], [[2, 5, 3, 11, 7]], [[2, 1, 6, 7, 8, 9]], [[18, 10, 6, 4]], [[2, 1, 3, 9]], [[0, 2, 4, 10, 17, 9, 5]], [[6, 4, 17, 2, 12]], [[21, 4, 7]], [[18, 1, 6]], [[2, 17, 3, 10, 9, 8, 6]], [[0, 2, 10, 9, 8, 6]], [[2, 1, 5, 18, 10, 7]], [[4, 2, 1, 12, 6, 7, 8, 9, 10]], [[0, 21, 2, 4, 10, 17, 9, 6, 5]], [[0, 2, 10, 16, 17, 9, 8, 5]], [[2, 1, 9]], [[1, 2, 9, 16, 7, 5, 6]], [[2, 1, 5, 0, 7, 10]], [[4, 2, 1, 6, 7, 8, 11, 9, 20, 10]], [[1, 2, 9, 19]], [[0, 10, 2, 9, 3, 14, 4, 7, 5, 6]], [[5, 7]], [[1, 6]], [[4, 2, 1, 19, 5, 14, 18, 12, 7]], [[21, 9, 5, 7]], [[6, 14, 1, 3, 7]], [[1, 2, 3, 9, 8, 6, 5]], [[3, 5, 2, 6, 8, 20]], [[2, 1, 5, 3, 10, 11, 4, 18]], [[1, 5, 7]], [[2, 1, 5, 13, 10]], [[18, 2, 1, 21, 3]], [[1, 19, 2, 5, 4, 7, 9, 8, 10]], [[4, 2, 3, 1, 18, 5, 6, 7]], [[1, 2, 18, 10, 6, 5]], [[17, 1, 2, 18, 9, 8, 7]], [[0, 2, 11, 10, 17, 9, 8, 6, 5]], [[18, 10, 9, 8, 1, 2, 3, 4, 7, 6, 5]], [[4, 2, 1, 5, 7, 14, 9, 10]], [[1, 2, 3, 9]], [[0, 2, 11, 17, 9, 8, 6, 5]], [[15, 10, 0]], [[4, 2, 1, 6, 8, 9]], [[4, 2, 1, 19, 6, 14, 18, 7]], [[13, 1, 2, 3, 6, 10, 9, 8, 7, 11, 5]], [[2, 0, 3, 10, 7]], [[16, 2, 3, 10, 9, 7, 6, 5]], [[9, 3, 7]], [[4, 2, 0, 6, 8, 9]], [[12, 1, 10, 2, 9, 14, 4, 7, 5, 6]], [[0, 2, 3, 4, 10, 17, 9, 8, 5]], [[1, 2, 20, 3, 9, 8, 6]], [[1, 2, 8, 3, 10, 9, 14, 5]], [[4, 2, 19, 5, 6]], [[20, 14, 4, 7]], [[2, 9, 14, 7, 5, 10, 6]], [[2, 3, 10, 9, 8, 7, 5]], [[1, 10, 8, 9, 7]], [[2, 8, 3, 7]], [[1, 13]], [[6, 14, 1, 7]], [[21, 1, 5, 7]], [[3, 18, 10, 6, 4]], [[4, 2, 1, 5, 7, 15, 9, 10]], [[2, 12, 3, 11, 10, 9, 8, 7, 5]], [[2, 3, 10, 9, 1, 7, 5]], [[17, 1, 2, 18, 21, 8, 7]], [[10, 1, 7]], [[18, 20, 14]], [[14, 3, 4, 7]], [[11, 2, 10, 7, 4]], [[4, 1, 3, 5, 6, 7]], [[2, 6, 4, 7]], [[17, 2, 18, 21, 8, 7]], [[0, 1, 6]], [[18, 1, 2, 3, 9, 8, 6, 5]], [[4, 1, 3, 18, 5, 6, 7]], [[1, 10, 2, 9, 14, 7, 4, 6]], [[2, 20, 10, 9, 8, 7, 5]], [[2, 1, 13]], [[2, 12, 11, 10, 9, 8, 7, 5]], [[3, 10, 8, 7, 6, 5]], [[1, 2, 9, 14, 7, 20, 10, 17]], [[4, 1, 6, 7, 5, 9]], [[1, 16, 14, 3, 18, 9, 8, 7, 5]], [[19, 2, 0, 11, 7]], [[1, 0, 2, 10, 8, 6, 5]], [[1, 2, 8, 10, 9, 14, 5]], [[1, 2, 18, 0, 7, 5]], [[18, 10, 6]], [[0, 1, 2, 4, 10, 21, 17, 9, 6, 5]], [[13, 1, 2, 3, 6, 10, 9, 7, 11]], [[1, 2, 10, 6, 5]], [[18, 0, 1]], [[5, 2, 6, 8, 20]], [[4, 2, 1, 5, 19, 8, 9]], [[6, 1, 16, 13]], [[18, 10, 14, 6, 4]], [[6, 1, 3, 11, 5, 7]], [[1, 2, 5, 7]], [[0, 1, 8, 2, 3, 7]], [[1, 9]], [[4, 2, 1, 5, 7, 13, 14, 9, 10]], [[4, 2, 19, 6]], [[2, 6, 14, 1, 7]], [[4, 15, 3, 5, 6, 7]], [[2, 17, 11, 3, 10, 8, 6, 5]], [[1, 3, 12, 10, 9, 8, 6, 15]], [[13, 1, 2, 3, 6, 10, 9, 8, 11, 7, 5]], [[0, 5, 3, 10, 7]], [[4, 2, 1, 5, 7, 9, 21, 10, 3]], [[1, 2, 13, 14, 7, 5, 6]], [[17, 4, 7]], [[1, 10, 2, 3, 8, 4, 7, 5, 6]], [[0, 14, 3, 18, 9, 7, 5]], [[4, 2, 11, 1, 5, 7, 15, 9, 10]], [[0, 2, 4, 17, 9, 5]], [[1, 3, 9, 8, 6, 5]], [[0, 5, 3, 7, 19, 10]], [[19, 2, 1, 8, 3, 11, 7]], [[12, 1, 10, 2, 9, 4, 7, 5, 6]], [[3, 4, 5, 2, 6, 8, 20]], [[4, 3, 2, 6, 7, 8, 11, 9]], [[1, 8, 9, 7]], [[2, 17, 11, 3, 10, 8, 15, 5]], [[1, 2, 9, 14, 7, 5, 0, 6]], [[7, 1, 3, 11, 13]], [[3, 6, 8, 9, 10]], [[3, 4, 2, 1, 6, 7, 8, 9, 20]], [[2, 5, 7]], [[16, 2, 3, 10, 9, 7, 6, 0, 5]], [[2, 1, 3]], [[0, -1, 21, 2, 4, 10, 17, 9, 6, 5]], [[2, 21, 10, 9, 8, 7, 5]], [[17, 18, 1, 21, 2]], [[2, 1, 7]], [[3, 5, 2, 19, 8, 21]], [[2, 1, 6, 5, 7, 10]], [[17, 1, 20, 3]], [[1, 2, 3, 6, 10, 9, 7, 11]], [[1, 10, 7, 5]], [[1, 2, 3, 9, 6, 12]], [[21, 5, 7]], [[21, 4, 1, 5]], [[12, 3, 11, 10, 9, 8, 7, 5]], [[1, 16, 14, 3, 19, 11, 13, 7, 5]], [[4, 1, 5, 7, 9, 10, 3]], [[3, 10, 8, 9, 6]], [[11, 7]], [[1, 3, 9, 8, 5]], [[5, 14, 3, 2, 9]], [[2, 6, 14, 4, 7]], [[1, 5, 3, 10, 11, 4, 18]], [[10, 2, 3, 8, 4, 7, 5, 6]], [[18, 0, 21, 1]], [[1, 3, 20]], [[18, 12, 3]], [[0, 2, 16, 7]], [[19, 2, 1, 3, 12, 10, 11, 7]], [[2, 6, 4]], [[4, 1, 5, 7, 8, 9]], [[1, 4]], [[14, 4, 17, 1, 5, 7, 8, 9, 10]], [[19, 1, 0, 11, 7]], [[4, 2, 1, 17, 19, 5, 14, 6]], [[14, 7]], [[14, 3, 2, 12]], [[10, 2, 11, 7]], [[2, 1, 6, 7, 8, 20, 10]], [[1, 3, 5, 4, 2, 6, 8, 7, 14, 10]], [[1, 9, 7]], [[14, 9, 1, 20, 15]], [[1, 20, 9, 8, 6]], [[0, 2, 10, 16, 17, 19, 9, 8, 5]], [[1, 8, 3, 10, 9, 7, 5]], [[1, 2, 4, 10, 17, 9, 6, 5]], [[1, 8, 9]], [[17, 1, 2, 18, 9, 8, 3, 7]], [[2, 1, 6, 7, 8, 20, 5, 10]], [[1, 5, 16, 7, 9, 10, 3]], [[0, 4, 17, 1, 5, 7, 8, 19, 10]], [[5, 2, 6, 12, 8, 20]], [[5, 3, 2, 1, 6, 7, 8, 9, 20, 10]], [[4, 2, 1, 6, 8, 13, 9, 10]], [[1, 2, 5, 4, 7, 6, 9, 8, 12]], [[1, -1, 3, 6, 10, 9, 7]], [[1, 5, 4, 7, 6, 8, 12, 2]], [[4, 3, 2, 1, 6, 7, 8, 11, 9, 10]], [[1, 2, 18, 9, 19]], [[2, 8, 5, 3, 7]], [[4, 2, 1, 3, 5, 6, 12, 7]], [[2, 1, 7, 10]], [[3, 5, 4, 2, 6, 9, 20, 10]], [[6, 19, 2, 11, 7]], [[10, 1, 17, 7]], [[13, 1, 2, 3, 6, 10, 9, 8, 5]], [[10, 8, 9, 7]], [[1, 4, 12]], [[4, 2, 0, 6, 7, 8, 9, 10]], [[2, 14, 11, 3, 10, 9, 8, 6, 5]], [[2, 1, 3, 11, 12, 7]], [[16, 2, 3, 10, 9, 8, 14, 6]], [[6, 4]], [[0, 14, 3, 18, 9, 7]], [[1, 2, 3, 18, 9, 6, 5]], [[2, 12, 0, 11, 10, 9, 8, 7, 5]], [[13, 11, 3, 6, 10, 9, 8, 5]], [[4, 1, 18, 5, 6, 7]], [[10, 18, 2, 3, 8, 4, 7, 5, 6]], [[18, 20, 3]], [[3, 14, 4, 7]], [[5, 14, 11, 3, 2, 12]], [[8, 1, 20, 3]], [[2, 1, 6, 7, 8, 10]], [[2, 6, 5, 7, 10]], [[1, 3, 9]], [[2, 20, 10, 7, 4]], [[18, 2, 1, 21]], [[4, 3, 1, 6, 8, 13, 19, 9, 10]], [[8, 1, 5, 3, 10, 7]]]
    results = [3, -1, 2, 4, -1, -1, -1, 4, 7, 9, 9, 2, 3, -1, 2, -1, 1, 8, -1, -1, 7, 3, 3, 1, 9, 8, 1, 2, 10, 1, 2, 1, 1, 3, 9, 1, 3, 8, 3, 8, 2, 3, 2, 2, 2, 3, 1, 8, 3, 3, 8, 1, 3, 2, -1, 3, 3, 2, 2, -1, -1, 3, 9, 3, 3, 4, 4, 7, 1, 2, 2, 4, 1, 1, 2, -1, 5, 2, 3, 9, 8, 9, 3, 2, 1, 4, -1, 2, -1, 9, 1, 1, -1, 5, -1, -1, 3, 4, -1, 2, 8, 13, 7, 8, 9, 8, 4, 8, 3, 3, 3, 8, 13, 8, 7, 3, 4, 8, 7, 6, 6, 8, 4, 4, 8, 1, 2, 3, 3, 1, 2, 9, 3, 2, 8, 9, 2, 8, 10, 6, -1, 3, 3, 7, 5, 6, 5, 5, 9, 4, 11, 1, 7, 8, 3, 4, 1, 8, 2, 2, 1, 7, -1, 12, 6, 7, 4, 4, -1, 5, 3, 9, 11, 4, -1, 3, 8, 3, 5, 1, 4, 3, 1, 12, 8, 2, 3, 7, 2, 4, -1, 3, 5, 4, 5, 1, 4, 4, -1, 5, 5, 2, 11, -1, 2, 1, 3, 7, 2, 3, 5, 5, 3, 1, 5, 8, 5, 3, -1, 2, -1, 2, 3, 8, 4, 4, -1, 3, 2, 1, 9, 1, 1, 7, 8, 5, 6, 3, 3, 6, 4, 6, 6, 5, 3, 3, 7, 11, 2, 3, 5, 4, 1, 7, 1, 3, 5, 2, 4, 5, 3, 3, 4, -1, 3, 5, 8, 8, 3, 3, 7, 2, 3, 6, 3, 3, 4, 6, 2, -1, -1, 6, 5, 2, 7, 2, 4, 2, 9, 3, 7, 7, 2, 1, 2, 1, 4, 2, 7, 6, 5, 2, 6, 5, 1, 3, 2, 9, 4, 9, 4, 4, 7, 8, 3, 2, 13, 3, 1, 7, 5, 3, 6, 8, 1, 5, 2, 2, 2, 3, 2, -1, 2, 1, 7, 4, 2, 2, 1, 1, -1, 4, -1, -1, 4, 1, 4, 4, 2, 1, 2, 2, 8, 3, 6, 5, 8, 3, 8, 3, 5, -1, 9, 5, 3, 2, 4, 5, 3, 1, 2, 1, 7, 3, 1, 2, 10, 5, 2, 8, 1, 2, 5, 3, 4, 7, 5, 3, 1, 2, 4, 1, 4, 6, 4, -1, 8, 3, 6, 2, 7, 9, 2, 5, 4, 3, 3, 4, 4, 2, 6, 7, 5, 3, 5, 5, 8, 1, 9, 4, 4, 4, 3, 2, 3, 7, 3, 5, 3, 5, 5, 5, 3, 3, 5, 3, 6, 5, 3, 6, 2, -1, 1, 4, 6, 1, -1, 1, 5, 2, 8, 8, 7, 3, 4, 4, 3, 1, 1, 6, 8, 7, 1, -1, 9, 8, 5, 4, 2, 3, 3, 5, 2, 5, 7, 4, 3, 1, 8, 7, 2, 2, 4, 3, 7, 3, 4, 4, 4, -1, 2, 2, 3, 5, 7, 3, 1, 7, 1, 6, -1, 4, 7, 13, 3, 4, 4, 2, 5, 1, 3, 3, 6, 4, 3, 4, 5, 2, 6, -1, 5, 4, 4, 5, -1, 4, 1, 9, 2, 5, 4, 6, 4, -1, 2, 4, 3, 4, 2, 3, 6, 9, 3, 3, 8, 4, 6, -1, 5, 3, 8, 5, 4, 4, 5, 2, -1, -1, 9, 4, 4, 2, 1, 1, 2, 7, 4, 4, 7, 5, 4, 6, 3, 6, 6, 3, 1, 5, -1, 4, -1, 5, 4, 5, 4, 12, 7, -1, 4, 7, 7, 8, 7, -1, 1, 8, 6, 7, 6, 5, 5, 3, 7, 6, 1, 5, 6, 8, 3, 3, 6, 6, 5, 8, 6, 3, 7, 8, 4, 2, 3, 5, 4, -1, 8, 5, 1, 6, 4, 7, 6, 12, 5, 4, 5, 1, 5, 7, 3, 6, 6, 3, 1, 2, 8, 2, 7, 6, 8, 7, 2, 5, 1, 7, 8, 5, 6, 8, 5, -1, 3, 1, 1, 4, 7, 7, 7, 1, 4, 5, -1, 4, 9, 2, 1, -1, 1, 2, 7, 3, 9, 6, 2, 4, 7, 7, 6, 2, 1, 7, 2, 1, 9, 1, 7, 4, 4, 3, 6, 7, 4, 8, 7, 4, 9, 3, 4, 2, 3, 6, 7, 2, -1, 3, 6, 5, -1, 3, 2, 7, 1, 5, 6, 6, 7, 5, -1, -1, 5, 5, 5, 4, 4, 7, 1, 5, 1, 2, 8, 2, 7, 5, 1, 7, 7, 3, 6, 8, 8, 3, 1, 3, 4, 7, 6, 4, 1, 3, 1, 6, 3, 1, 1, 6, 5, 5, 4, 8, 7, 1, 5, 3, 9, -1, 8, -1, -1, 8, 2, 2, 6, 2, 6, -1, 4, 4, 7, 5, 5, 6, 8, 10, 6, -1, 7, 2, 2, 7, 10, 4, 7, 1, 2, 8, 8, 6, 7, 3, 2, 6, 6, 4, 2, -1, 2, 1, 4, 6, 8, 6, 6, 1, 2, 1, 4, 1, 2, 5, -1, 7, 4, 6, 6, 1, 7, 5, 6, 4, 8, 4, 6, 6, 5, 2, 9, 7, 4, 1, 1, 5, 3, 4, 4, -1, 3, -1, 7, 3, 3, 2, 7, 6, 10, 4, 8, 5, 1, 7, 6, 7, 5, 5, 5, 6, 7, 3, 7, 3, 7, 6, 1, -1, 3, -1, 7, 1, 9, 6, 4, 1, 4, 3, 3, 6, 3, 4, 1, 2, 7, 8, 6, 4, 1, 4, 3, 3, 5, 6, 3, -1, 2, 3, 7, 2, 1, -1, 3, 4, 7, 1, 2, 3, 6, 9, 2, 4, 4, 8, 6, 7, -1, 6, 6, 6, 8, 4, 9, 6, 7, 6, 7, 8, 3, 3, 7, 1, 7, 4, 3, 8, 3, -1, 2, 8, 5, 7, 1, 5, 6, 8, 7, 3, 7, 2, 2, 4, 3, 1, 2, -1, 4, 2, 7, 5]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(can_arrange)