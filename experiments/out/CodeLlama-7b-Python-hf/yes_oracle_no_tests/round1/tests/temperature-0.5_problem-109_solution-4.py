def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    
	Include these tokens in the code:   sorted _ arr = sorted (
	"""

    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def move_one_ball(arr):
        for i in range(len(arr)):
            arr.append(arr.pop(0))
            if is_sorted(arr):
                return True
        return False


    return move_one_ball(arr)


def move_one_ball2(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    
	Include these tokens in the code:   sorted _ arr = sorted (
	"""

    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] >



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
    inputs = [[[3, 4, 5, 1, 2]], [[3, 5, 10, 1, 2]], [[4, 3, 1, 2]], [[3, 5, 4, 1, 2]], [[]], [[1]], [[5, 6, 7, 8, 1, 2, 3, 4]], [[1, 2, 3, 4, 5, 6, 7, 8]], [[8, 7, 6, 5, 4, 3, 2, 1]], [[2, 1]], [[4, 3, 2, 1]], [[9, 7, 8, 6, 4, 5, 3, 1, 2]], [[3, 2, 1, 4, 5]], [[1, 2, 3, 4, 5]], [[5, 4, 3, 2, 1]], [[5, 6, 7, 8, 1, 2, 4]], [[5, 4, 3, 2]], [[8, 7, 6, 5, 4, 2, 1]], [[9, 2, 1]], [[1, 2, 3, 4]], [[5, 6, 8, 1, 2, 4]], [[6, 7, 8, 1, 2, 3, 4]], [[9, 2, 6]], [[5, 6, 8, 2, 4]], [[4, 3, 2]], [[86, 5, 9, 2, 4]], [[9, 5, 2, 6]], [[8, 7, 6, 5, 3, 1]], [[1, 2, 3]], [[86, 5, 2, 4]], [[8, 7, 6, 5, 3, 2]], [[7, 8, 6, 4, 5, 3, 1, 2]], [[4, 1]], [[8, 1]], [[3, 2, 1]], [[4, 3]], [[2, 1, 4, 5]], [[9, 7, 8, 5, 4, 3, 1, 2]], [[7, 6, 5, 4, 2, 1]], [[9, 4, 1]], [[86, 5, 2]], [[6, 2, 1, 4]], [[8]], [[3]], [[4]], [[1, 3]], [[7, 5, 4, 3]], [[2]], [[3, 5, 1]], [[3, 4]], [[3, 2, 4, 5]], [[1, 2]], [[2, 3, 1, 4, 5]], [[13]], [[86, 7, 6, 5, 4, 2, 1]], [[2, 3, 1, 5]], [[8, 7, 5, 3, 2]], [[5, 2]], [[2, 4, 5]], [[8, 2, 1, 4, 5]], [[9, 7, 6, 4, 5, 3, 1, 2]], [[5, 8, 2, 4]], [[9, 7, 8, 5, 4, 86, 3, 1, 2]], [[2, 8, 7, 6, 5, 3, 1]], [[2, 6, 9]], [[9, 2]], [[9, 7, 8, 5, 4, 6, 1, 2]], [[7, 6, 4, 5, 3, 1, 2]], [[3, 2, 6, 9]], [[1, 3, 2, 6]], [[5, 6, 7, 8, 1, 2, 3]], [[9, 7, 13, 5, 4, 6, 1, 2]], [[8, 7, 13, 6, 2]], [[8, 7, 6, 3, 2]], [[5, 6, 8, 7, 2, 3]], [[1, 7, 3]], [[3, 5]], [[6, 7, 8, 1, 3, 4]], [[6, 7, 8, 1, 2, 4]], [[9, 6, 7, 8, 1, 2, 3]], [[8, 7, 14, 6, 2]], [[3, 2]], [[86, 4, 1]], [[8, 7, 2, 6, 5, 3]], [[5, 6, 8, 7, 2, 4]], [[6, 8, 7, 13, 86]], [[5, 3, 2, 6, 7, 1, 8, 4]], [[1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12]], [[1, 4, 7, 8, 5, 3, 2, 6]], [[1, 2, 3, 4, 5, 6, 7, 9, 8]], [[1, 3, 2, 5, 4, 7, 6, 9, 8]], [[-2, 0, 2, 1, 3, 8, 7, 6, 5, 4]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[0, 1, 6, 2, 5, 8, 7, 4, 3]], [[5, 3, 2, 6, 7, 1, 4]], [[1, 3, 2, 4, 7, 6, 9, 8]], [[1, 3, 2, 4, 7, 6, 9, 11, 8]], [[1, 3, 2, 4, 7, 6, 9, 0, 8]], [[5, 3, 6, 7, 1, 8, 4]], [[1, -2, 7, 8, 5, 3, 2, 6]], [[1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12]], [[0, 1, 6, 2, 5, 8, 7, 3]], [[1, -2, 7, 8, 5, 3, 6]], [[5, 3, 6, 7, 0, 8, 4]], [[1, 3, 2, 4, 6, 9, 0, 8]], [[0, 1, 6, 5, 8, 7, 4, 3]], [[1, 3, 4, 5, 6, 7, 8]], [[1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 13]], [[3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12]], [[1, 3, 5, 7, 10, 11, 2, 4, 6, 8, 12]], [[5, 7, 9, 11, 2, 4, 6, 8, 10, 12]], [[4, 7, 8, 5, 3, 2, 6]], [[1, 4, 5, 6, 7, 8]], [[1, 3, 0, 7, 9, 11, 2, 4, 6, 8, 10, 13]], [[5, 2, 6, 1, 8, 4]], [[1, 3, 2, 4, 7, 6, 11, 8]], [[1, 4, 5, 6, 7]], [[1, 2, 4, 7, 6]], [[9, 5, 7, 10, 11, 2, 4, 6, 8, 12]], [[3, 2, 7, 4, 6, 9, 0, 8]], [[1, 3, 2, 4, 6, 9, -1, 0, 8]], [[11, 1, 0, 5, 6, 7, 8]], [[3, 5, 7, 9, 11, 2, 4, 6, 8, 10]], [[1, 3, 2, 4, 6, -1, 0, 8]], [[3, 2, 4, 6, -1, 0, 8, 1]], [[1, 3, 2, 4, 6, 9, 8]], [[2, 5, 4, 7, 6, 9, 8]], [[-2, 0, 2, 1, 3, 8, 6, 5, 4]], [[1, 4, 5, 3, 6, 7]], [[7, 1, 3, 2, 4, 6, -1, 0, 8]], [[5, 3, 2, 6, 8, 1, 4]], [[10, 0, 1, 6, 2, 5, -1, 8, 7, 3]], [[5, 3, 6, 7, 1, 4]], [[8, 7, 6, 5, 4, 3, 2]], [[1, -2, 7, 4, 3, 2, 6]], [[5, 3, 6, 7, 1, 8]], [[5, 3, 6, 0, 8]], [[1, -2, 11, 8, 5, 3, 2, 6]], [[3, 5, 7, 10, 13, 11, 2, 4, 6, 8, 12]], [[1, 3, 2, 4, 7, 9, 0, 8]], [[1, 3, 2, 4, 7, 6, 9]], [[5, 7, 9, 2, 4, 6, 8, 10, 12]], [[8, 7, 5, 4, 2, 1]], [[0, 1, 6, 5, 2, 8, 7, 4, 3]], [[1, 5, 2, 4, 7, 6, 9]], [[5, 3, 0, 8]], [[4, 8, 5, 3, 2, 6]], [[1, 2, 3, 4, 5, 6, 9, 8]], [[5, 3, 2, 6, 7, 8, 1, 4]], [[5, 7, 9, 11, 2, 6, 8, 10, 12]], [[0, 1, 6, 8, 7, 4, 3]], [[5, 2, 6, 1, 7, 4]], [[5, 3, 6, 2, 1, 8, 4]], [[10, 5, 3, 6, 7, 1, 4]], [[1, 3, 2, 4, 7, 6, 9, 12, 8]], [[1, 3, 5, 7, 11, 2, 4, 8, 12]], [[1, 3, 2, 7, 6, 9, 11, 8]], [[1, 3, 5, 11, 2, 4, 8, 12]], [[1, 11, 8, 5, 3, 2, 6]], [[5, 7, 9, 11, 2, 4, 6, 8, 10]], [[1, 3, 5, 7, 11, 2, 8, 6, 12]], [[1, 3, 5, 4, 7, 6, 9, 8]], [[1, 8, 5, 3, 2, 6]], [[10, 1, -2, 7, 3, 5, 2, 6]], [[5, 7, 9, 3, 2, 4, 6, 8, 10, 12]], [[1, 4, 7, 6]], [[5, 7, 11, 2, 6, 8, 10, 12]], [[1, -2, 6, 8, 5, 3, 2, 13]], [[0, 1, 6, 2, 5, 8, 7, 13, 3]], [[1, 4, 6]], [[1, -2, 8, 5, 3, 2]], [[4, 6]], [[4, 5, 3, 6, 8]], [[3, 5, 7, 10, 13, 11, 2, 4, 8, 12]], [[3, 5, 7, 9, 11, 2, 4, 6, 10, 13]], [[7, 6]], [[-2, 11, 8, 5, 3, 2, 6]], [[5, 12, 6, 7, 1, 8, 4]], [[3, 11, 6]], [[5, 3, 2, 6, 7, 0, 4]], [[1, 3, 5, 7, 11, 2, 10, 4, 8, 12]], [[5, 2, 10, 1, 4]], [[3, 2, 7, 4, 6, 9, 0]], [[3, 5, 4, 7, 6, 8]], [[5, 3, 6, 7, 4]], [[4, 5, 7, 3, 6, 8]], [[3, 2, 4, 6, 9, 0, 8]], [[10, 3, 6, 7, 1, 4]], [[5, 3, 6, 7, 0, 8]], [[3, 8, 7, 5, 4, 2]], [[10, 2, 3, 6, 7, 1, 12, 4]], [[4, 8, 5, 3, 2]], [[8, 1, 2, 4, 7, 6]], [[5, 3, 6, 1, 12, 7, 4]], [[-2, 3, 2, 4, 6, -1, 0, 8]], [[5, 2, 7, 1, 3]], [[11, 1, 0, 5, 6, 10, 7, 8]], [[1, 3, 2, 4, 6, -1, 0, -2]], [[5, 3, 6, 7, 0, 8, 4, 2]], [[1, 5, 11, 2, 4, 8, 12]], [[5, 3, 7, 1, 8, 6]], [[8, 7, 6, 11, 4, 3, 2, 1]], [[5, 3, 2, 6, 7, 0, 10]], [[5, 7, 9, 11, 2, 4, 8, 10, 12]], [[5, 2, 1, 3]], [[11, 8, 5, 3, 2, 6]], [[3, 11, 0, 6]], [[1, 5, 3, 0, 8]], [[1, 4, 5, 6, 8]], [[11, 1, 0, 6, 10, 7, 8]], [[1, 4, 5, 3, 6]], [[1, 3, 4, 5, 6, 8]], [[55, 22, 7, 10]], [[-1, 8, 6, 7, 1, 4, 3]], [[7, 6, 11, 4, 3, 2, 1]], [[5, 1, 3]], [[1, 3, 4, 5, 6, 2, 8]], [[1, 3, 11, 4, 8, 12]], [[11, 6]], [[8, 14, 7, 13, 6, 5, 2, 1]], [[3, 5, 7, 11, 2, 10, 4, 8, 12]], [[0, 1, 4, 6]], [[11, 13, 1, 0, 6, 10, 7, 8]], [[5, 2, 8, 6, 1, 22, 4]], [[9, 5, 7, 11, 2, 4, 6, 8, 12]], [[3, 5, 7, 9, 11, 2, 6, 10, 8]], [[1, 5, 4, 7, 6, 9]], [[11, 13, 1, 6, 10, 8]], [[1, 3, 5, 9, 7, 10, 11, 2, 4, 6, 8, 12]], [[3, 5, 7, 9, 11, 2, 4, 6, 8, 0, 12]], [[5, 3, 6, 4, 1, 8]], [[5, 3, 6, 1, 14, 7, 4]], [[5, 3]], [[-2, 7, 8, 5, 3, 2, 6]], [[11, 13, 6]], [[-2, 3, 1, 4, 6, -1, 0, 8]], [[1, -2, 11, 8, 5, 3, 2]], [[1, 0, 6, 10, 3, 8]], [[0, 1, 6, 5, 2, 7, 4, 3]], [[3, 5, 7, 9, 11, 2, 10, 14, 8]], [[-2, 3, 1, 4, 6, -1, 0]], [[5, 3, 6, 7]], [[6, 2, 1, 3]], [[1, 3, 5, 7, 9, 11, 55, 4, 6, 8, 10, 12]], [[10, 3, 7, 1, 4]], [[0, 13, 1, 6, 2, 5, 8, 7, 3]], [[1, 3, 2, 5, -2, 4, 7, 6, 9, 8]], [[5, 7, 9, 11, 2, 4, 6, 8, 12]], [[3, 4, 5, 6, 2, 8]], [[6]], [[3, 2, 4, 7, 6, 11, 8]], [[3, 5, 7, 9, 11, 2, 6, 8, 10, 12]], [[1, 2, 0, 7, 6, 4]], [[5, 6, 1, 8, 4]], [[2, 7, 1, 8, 6]], [[5, 2, 4, 7, 6, 9]], [[3, 5, 7, 9, 11, 2, 10, 14]], [[3, 22, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12]], [[55, 22, 7]], [[3, 55, 0, 6]], [[3, 2, 4, 7, 9, 0, 8]], [[8, 1, 2, 3, 7, 6]], [[5, 3, 7, 8, 6]], [[5, 0, 6, 7, 13, 11, 4]], [[3, 2, 4, 7, 6, 8]], [[1, 2, 4, 6, 9, 8]], [[5, 7, 9, 2, 6, 8, 10, 12]], [[0, 1, 6, 2, 5, 9, 7, 13, 3]], [[3, 7, 1, 8]], [[9, 4, 5]], [[1, 4, 5, 6]], [[1, 3, 0, 7, 9, 11, 2, 4, 6, 10, 13]], [[1, 3, 2, 5, 7, 6, 9, 11, 8]], [[12, 5, 2, 6, 1]], [[22, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12]], [[8, 5, 2, 7, 1, 3]], [[5, 7, 2, 6, 8, 10]], [[0, 1, 2, 5, 8, 7, 3]], [[0, 6, 8, 7, 4, 3]], [[1, 5, 4, 7, 6]], [[1, 3, 2, 4, 6, 14, -1, 0, 8]], [[1, 3, 5, 7, 11, 2, 10, 4, 8]], [[8, 5, 14, 7, 1, 3]], [[3, 4, 6, -1, 0, 8, 1]], [[8, 7, 6, 5, 3, 2, 1]], [[8, 6, 5, 3, 2, 1]], [[-2, 2, 1, 3, 8, 7, 6, 5, 4]], [[3, 6, 7, 0, 8]], [[1, 3, 2, 4, 9, 8]], [[1, 3, 4, 7, 6, 9, 12, 8]], [[3, 2, 4, 7, 6, 9]], [[1, 2, 4, 9, 8]], [[11, 13, 6, 10, 8]], [[1, 8, 4, 3, 2, 6, 5]], [[4, 3, 7, 1, 8, 6]], [[1, 2, 3, 5, 4, 7, 6, 9, 8]], [[0, 1, 6, 2, 5, 9, 7, 13, 12, 3]], [[9, 4, 22, 5]], [[5, 7, 9, 11, 2, 4, 6, 8, 13, 10]], [[55, 21, 7]], [[5, 3, 7, 8, 10]], [[8, 7, 6]], [[5, 3, 6, -1, 7, 0, 8, 4]], [[5, 2, 14, 6, 7, 0, 10]], [[-2, 0, 2, 1, 3, 7, 6, 5, 4]], [[1, 3, 5, 7, 11, 8, 6, 12]], [[8, 10, 7, 6, 5, 4, 3, 2]], [[1, 2, 6, 9, 8]], [[22, 5, 3, 6, 7]], [[8, 7, -1, 11, 4, 3, 2, 1]], [[3, 6, 7, 0, 5, 8, 4]], [[5, 2, 6, 1, 7]], [[13, 3, 5, 7, 9, 11, 2, 6, 8, 10, 12]], [[1, -2, 8, 5, 3, 2, -1]], [[3, 2, 4, -1, 0, 8, 1]], [[1, 3, 5, 7, 11, 2, 10, 4, 6]], [[-2, 4, 6, -1, 0]], [[5, 3, 8, 6]], [[8, 19, 6, 89, 7]], [[11, 1, 0, 6, 10, 7]], [[5, 7, 1, 9, 11, 2, 6, 8, 10, 12]], [[6, 3]], [[1, 4, 5, 6, 12, 8]], [[1, 0, 6, 3, 8]], [[7, 3, 2, 4, 6, 9, -1, 0, 8]], [[-2, 3, 7, 8, 6]], [[3, 6, -1, 0, 8, 1]], [[5, 3, 2, 7, 1, 8, 4]], [[1, 10, 4, 5, 6, 7, 8]], [[4, 8, 5, 55, 3, 6]], [[-2, 3, 10, 4, 6, -1, 0, 8]], [[1, -2, 11, 5, 3, 2]], [[3, 2, 4, 6, 9, 8]], [[10, 3, 6, 8, 1, 4]], [[1, 3, 2, 4, 21, 7, 6, 11, 8]], [[-2, 0, 2, 3, 8, 5, 4]], [[1, 3, 11, 4, 8, -1]], [[3, 2, 4, 9, 0, 8]], [[1, 5, 3, 2, 6]], [[10, 0, 1, 6, 2, 5, 8, 7, 3]], [[8, 1, 2, 3, 7]], [[5, 3, 2, 11, 1, 8, 4]], [[3, 6, 0, 5, 8, 4]], [[1, 5, 3, 0, 9]], [[1, 13, 7, 4, 3, 2, 6]], [[5, 3, 6, 1, 7, 4]], [[5, 3, 6, 7, 1, 8, 10, 4, 9]], [[7, 1, 3, 2, 4, 6, -1, 8]], [[0, 8, 1, 6, 2, 5, 9, 7, 13, 3]], [[1, 4, 7]], [[2, 3, 4, 5, 6, 9, 8]], [[14, 0, 6, 8]], [[3, 10, 4, 6, -1, 0, 8]], [[1, 4, 6, 7]], [[5, 3, 6, 2, 10, 4]], [[5, 2, 3]], [[5, 3, 6, 7, 0, 9, 4, 2]], [[3, 7, 9, 11, 2, 10, 14, 8]], [[5, 3, 7]], [[1, 3, 2, 14, 7, 6, 9, 8]], [[1, 2, 5, 4, 7, 19, 9, 8]], [[1, 3, 2, 14, 6, 9, 8]], [[5, 3, 6, 7, -2]], [[5, 0, 9, 11, 2, 6, 8, 10, 12]], [[1, 8, 5, 3, 2, -1]], [[11, 13]], [[5, 3, 9, 6]], [[5, 2, 4, 10, 6, 9]], [[1, 4, 11, 6]], [[-2, 2, 1, 8, 7, 6, 5, 4]], [[3, 5, 7, 10, 13, 11, 2, 4, 9, 12]], [[3, 4, 8, 12]], [[21]], [[-2, 11, 8, 5, 21, 3, 2, 6]], [[55, 22, 10]], [[1, 7, 8, 5, 3, 2, 6]], [[3, 5, 4, 6, 8]], [[1, 13, 7, -2, 3, 2, 6]], [[3, 4, 8]], [[55, 7, 10]], [[3, 2, 7, 6, 9, 0]], [[3, 2, 4, 7, 5, 6, 11, 8]], [[11, 0, 13, 1, 6, 10, 8]], [[-2, 11, 8, 5, 21, 3, 2]], [[0, 1, 6, 14, 7, 4, 3]], [[55, 21, 8, 7]], [[2, 12, 6]], [[5, 3, 7, 13, 8, 10]], [[5, 2, 4, 10, 8, 9]], [[10, 3, 1, 4]], [[3, 2, 4, 6, 0, 8]], [[3, 2, 4, 7, 6, 1, 11, 8]], [[1, 3, 2, 4, 21, 7, 6, 8]], [[1, 5, 0, 6, 7]], [[12, 3, 11, 6]], [[3, 5, 7, 9, 11, 1, 6, 10, 8]], [[3, 4, 6, -1, 19, 8, 1]], [[10, 1, 6, 2, 5, 8, 7, 3]], [[11, 89, 8, 5, 3, 2, 6]], [[5, 7, 9, 11, 6, 8, 10, 12]], [[3, 6, 0, 7, 5, 8, 4]], [[5, 7, 9, 11, 2, 4, 6, 8, 0, 12]], [[4, 5, 14, 6, 8]], [[2, 6, 1, 8, 4]], [[0, 1, 6, 5, 9, 7, 13, 3]], [[5, 13, 3, 8, 6]], [[3, 5, 7, 8, 10, 13, 11, 2, 4, 9, 12]], [[1, 3, 4, 5, 6, 9]], [[1, 3, 9, 7, 10, 11, 2, 4, 6, 8, 12]], [[5, 1, 9, 11, 2, 6, 8, 10, 12]], [[1, 3, 2, 4, 14, -1, 0, 8]], [[1, 55, 5, 2, 0, 9]], [[1, 4, 7, 9]], [[5, 3, 55, 7, 0, 8, 4, 2]], [[12, 0, 1, 5, 8, 7, 10]], [[4, 3, 6, 7, 1, 8]], [[89, 5, 3, 6, 7, 1, 8]], [[5, 2, 8, 6]], [[7, 2, 4, 6, -1, 0, 8]], [[3, 2, 4, 7, 89, 8]], [[3, 14]], [[1, 3, 2, 7, 6, 9]], [[1, 3, 2, -2, 14, 7, 6, 9, 8]], [[4, 8, 5, 55, 2, 6]], [[4, 5, 55, 6, 8]], [[55, 22, 4, 10]], [[0, 1, 6, 2, 5, 9, 7, -1, 13, 3]], [[7, 1, 3, -2, 4, 6, -1, 8]], [[5, 3, 6, 1, 0, 14, 7, 4]], [[4, 89, 5, 3, 6, 7, 1, 8]], [[3, 4, 9, 0, 8]], [[3, 2, 4, 6, 11, 8]], [[5, 6, 1, 8, 3]], [[0, 2, 5, 8, 7, 13, 3]], [[1, 3, 11, 4, 8, 89]], [[22, 4, 5, 55, 6, 8]], [[1, 4, 5, 6, 12, 13, 8]], [[8, 3, 4, 5, 6, 9]], [[3, 5, 7, 10, -2, 11, 2, 4, 8, 12]], [[8, 3, 2, 6]], [[5, 7]], [[8, 14, 7, 13, 6, 5, 2]], [[1, 3, 5, 9, 7, 10, 11, 2, 13, 4, 6, 8, 12]], [[7, 4]], [[55, 21, 2, 8, 7]], [[1, 3, 7, 11, 2, 10, 4, 8]], [[4, 6, 5]], [[0, 13, 1, 4, 6, 2, 5, 8, 7, 3]], [[5, 1, 0, 6, 10, 3, 8]], [[1, 4, 14, 5, 6]], [[9, 5, 7, 10, 11, 2, 19, 6, 8, 12]], [[1, 3, 11, 4, 19, 8, 12]], [[5, 2, 6, 1, 0, 3]], [[1, 3, 2, 4, 6, 9]], [[2, 10, 1, 4]], [[1, 5, 2, 0, 9]], [[1, 12, 8, 5, 3, 2, 6]], [[5, 3, 7, 13, 10]], [[5, 2, 4, 10, 9]], [[1, 6, 3, 2, 4, 14, -1, 0, 8]], [[1, 4, 7, 8, 5, 3, 2]], [[0, 1, 6, 14, 2, 10, 8, 7, 3]], [[5, 3, 2, 7, 8, 4, 1]], [[1, 3, 2, 4, 7, 9, 11, 8]], [[55, 2, 8, 7]], [[0, 6, 4, 1, 8]], [[-2, 11, 5, 3, 2, 6]], [[55, 2, 89, 7]], [[1, 3, 11, 4, 8, 0, 89]], [[8, 5, 13, 2, 7, 1, 3]], [[5, 55, 7, 0, 8, 4, 2]], [[7, 1, 3, -2, 4, 6, 8]], [[1, 3, 5, 7, 11, 4, 8, 12]], [[10, 14, 8, 7, 6, 5, 4, 3, 2, 1]], [[12, 3, 11, 13, 8]], [[5, 3, 2, 7, 14, 1, 8, 4]], [[7, 5]], [[1, 4, 5, 9, 3, 6]], [[12, 6, 7, 1, 8, 4]], [[1, 3, 4, 8, 89]], [[11, 1, 0, 6, 7, 8]], [[1, 2, 3, 5, 6, 7, 8]], [[3, 4, 6, -1, -2, 0]], [[-2, 3, 1, 4, 13, -1, 0]], [[5, -1, 3]], [[0, 1, 6, 2, 5, 8, 7, 4]], [[0, 1, 6, 2, 5, 9, 7, 11, -2, 3]], [[8, 2, 3, 7, 6]], [[5, 0, 2, 10, 1, 4]], [[5, 3, 55, 2, 6, 7, 4]], [[5, 3, 6, 7, 0, 89, 8, 4]], [[-2, 2, 1, 3, 89, 7, 6, 5, 19, 4]], [[1, 3, 2, 19, 4, 7, 6, 11, 8]], [[4, 5, 6, 1, 2, 3]], [[2, 3, 1]], [[1, 3, 2]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]], [[50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[1, 2, 3, 4, 5, -2, 7, 9, 8]], [[1, 2, 4, -2, 7, 9, 8]], [[7, 6, 5, 4, 3, 2, 1]], [[1, 2, 3, 4, 5, 6, 11, 8]], [[-2, 0, 2, 1, 3, 8, 7, 6, 4]], [[2, 3, 4, -2, 7, 9, 8]], [[1, 2, 3, 4, 5, -2, 6, 11, 8]], [[1, 4, 7, 8, 9, 5, 3, 2, 6]], [[1, 4, -2, 7, 9, 8]], [[1, 3, 5, 7, 6, 9, 8]], [[5, 3, 2, 9, 7, 1, 8, 4]], [[1, 3, 5, 7, 6, 9]], [[1, 2, 4, 9, 7, 0, 8]], [[9, 1, 6, 2, 5, 8, 7, 4, 3]], [[1, 2, 3, 4, 5, -2, 9, 8]], [[1, 7, 2, 3, 4, 5, 6, 8]], [[1, 2, 4, 7, 9, 8]], [[3, 5, 7, 6, 8, 11, 12, 9]], [[3, 5, 7, 6, 8, 11, 12, 4]], [[1, 2, 3, 4, 5, 6, 8]], [[1, 2, 4, 0, -2, 7, 9, 8]], [[8, 7, 5, 4, 3, 2, 1]], [[5, 3, 2, 9, 7, 10, 1, 8, 4]], [[9, 1, 6, 2, 8, 7, 4, 3]], [[10, 9, 8, 7, 6, 5, -2, 2, 1]], [[1, 3, 5, 4, 7, 6, 9]], [[1, 2, 3, 4, 11, 5, 6, 7, 9, 8]], [[1, 2, 4, 5, 6, 7, 8]], [[1, 2, 4, 9, 0, 8]], [[1, 3, 4, 5, -2, 6, 11, 8]], [[2, 3, 5, -2, 7, 9, 8]], [[1, 2, 7, 4, 5, -2, 6, 11, 8]], [[8, 7, 5, 3, 0, 2, 1]], [[8, 7, 5, 10, 0, 2, 1]], [[1, 2, 4, 0, -2, 7, 8]], [[10, 9, 8, 7, 6, -2, 2, 1]], [[-2, 1, 2, 5, 4, 7, 6, 9, 8]], [[5, 2, 7, 10, 1, 8, 4, 9]], [[1, 2, 7, 0, 8]], [[10, 1, 2, 4, -2, 7, 9, 8]], [[5, 7, 6, 8, 11, 12, 4]], [[1, 2, -2, 7, 9, 6]], [[4, 5, 7, 6, 8, 11, 12, 10]], [[10, 1, 2, 5, -2, 7, 9, 8]], [[5, 2, 7, 10, 1, 8, 4]], [[1, 4, 8, 9, 5, 3, 2, 6]], [[5, 7, 6, 8, 11, 12, 10]], [[8, 7, 5, 10, 0, 2]], [[1, 2, 7, 8]], [[1, 2, 7, 0]], [[8, 7, 5, 3, 10, 0, 2]], [[1, 4, 8, 5, 3]], [[1, 2, 4, -2, 7, 10, 8]], [[5, 7, 6, 8, 3, 11, 10]], [[1, 3, 5, 7, 2, 9]], [[10, 9, 8, 7, 6, -2, 4, 2, 1]], [[1, 2, 3, 10, 4, 11, 5, 6, 7, 9, 8]], [[1, 2, 4, 7, 0, 8]], [[1, 2, 0, 3, 4, 5, -2, 6, 11, 8]], [[5, 7, 6, 11, 10]], [[1, 4, 5, 7, 6, 9]], [[8, 6, 5, 4, 3, 2, 1]], [[1, 3, 4, 5, 6, 11, 8]], [[3, 5, 6, 8, 11, 12, 9]], [[7, 6, 5, 4, 3, 12, 1]], [[5, 7, 9, 10, 1, 8, 4]], [[1, 3, 6, 7, 9, 8]], [[9, 0, 1, 12, 6, 2, 5, 8, 7, 4, 3]], [[1, 3, 4, 7, 0]], [[1, 2, 3, 4, 5, -2, 7, 8]], [[1, 2, 4, 12, 7, 0, 8]], [[2, 3, 4, 5, 6, -2, 7, 8]], [[9, 1, 6, 5, 8, 7, 4, 3]], [[3, 5, 7, 6, 1, 8, 11, 12, 4]], [[3, 5, 7, 8, 11, 12, 4]], [[8, 7, 5, 4, 3, 2, 0, 1]], [[1, 2, 4, 5, 6, 7, -2]], [[8, 7, 5, 3, 0, 2]], [[-2, 0, 2, 1, 8, 7, 6, 5, 4]], [[1, 9, 3, 4, 5, -2, 6, 11, 8]], [[0, 1, 12, 6, 2, 5, 8, 7, 4, 3]], [[8, 6, 5, 10, 0, 2]], [[1, 3, 5, 7, 11, 2, 4, 6, 8, 10, 12]], [[9, 0, 1, 12, 6, 2, 8, 7, 4, 3]], [[11, 1, 3, 4, 7, 0]], [[-2, 2, 5, 4, 7, 6, 9, 8]], [[1, 3, 2, 5, 4, 7, 9, 8]], [[8, 6, 1, 5, 10, 0, 2]], [[1, 2, 5, 7, 9, 6, 8]], [[-2, 0, -1, 2, 1, 8, 7, 6, 5, 4]], [[9, 0, 1, 12, 6, 11, 5, 8, 7, 4, 3]], [[7, 6, 5, 3, 12, 1]], [[1, 3, 2, 5, 4, 7, 8]], [[5, 3, 2, 9, 1, 8, 4]], [[-2, 0, 2, 1, 3, 10, 7, 6, 4]], [[1, 12, 3, 4, 7, 0]], [[9, 0, 1, 12, 6, 5, 8, 7, 4, 3]], [[5, 3, 2, 9, 7, 10, 1, 12, 8, 4]], [[-2, 2, 5, 4, 7, 6, 9]], [[10, 1, -1, 4, -2, 7, 9, 8]], [[9, 0, 1, 12, 6, 11, 5, 8, 7, 3]], [[10, 5, 4, 7, 6, 9]], [[1, 4, 5, 7, 6, 8, 9]], [[7, 6, 5, 3, 12]], [[7, 8, 6, 1, 5, 10, 0, 2]], [[8, 7, 5, 0, 2]], [[8, 7, 5, 3, 0, 1]], [[1, 4, 8, 5, 3, 2]], [[5, 3, 2, 6, 7, 1, 0, 8, 4]], [[5, 3, 2, 9, 8, 4]], [[7, 6, 5, 3]], [[9, 1, 6, 2, 5, -2, 8, 7, 4, 3]], [[3, 6, 10, 11, 12, 9, 5]], [[5, 11, 2, 7, 10, 1, 8, 4, 9]], [[1, 2, 5, 7, 9, 8]], [[1, 3, 4, 5, -2, 6, 2, 11, 8]], [[3, 6, 10, 11, 12, 7, 9, 5]], [[2, 3, 4, 5, -2, 7, 8]], [[3, 2, 6, 7, 1, 8, 4]], [[9, 1, 12, 6, 11, 5, 8, 7, 4, 3]], [[9, 1, 6, 5, 8, 7, 4]], [[1, 3, 2, 5, 4, 8]], [[11, 2, 4, 7, -1, 8]], [[9, 0, 1, 2, 12, 6, 5, 8, 7, 4, 3]], [[5, 2, 7, 10, 1, 4, 9]], [[1, 4, 8, 9, 5, 2, 6]], [[12, 1, 3, 2, 5, 4, 8]], [[5, 7, 6, 10]], [[11, 2, 4, 7, 8]], [[0, 5, 2, 7, 1, 8, 4]], [[0, 1, 2, 12, 6, 5, 8, 7, 4, 3]], [[2, 12, 3, 4, 7, 0]], [[1, 9, 3, 5, -2, 6, 11, 8]], [[8, 7, 5, 11, 0, 2]], [[1, 3, 5, 7, 4, 2, 9]], [[4, 7, 6, 8, 3, 11, 10]], [[2, 9, 3, 4, 7, 0]], [[10, 1, 2, 7, 9, 6, 8]], [[3, 5, 8, 11, 10, 4]], [[5, 7, 9, 10, 1, 8]], [[8, 6, 1, 10, 0, 2]], [[2, 4, -2, 7, 9, 8]], [[1, 3, -3, 9, -2, 7, 10, 8]], [[3, 4, -2, 7, 9, 8]], [[8, 7, 6, 5, 3, 4, 1]], [[8, 7, 6, 5, 9, 3, 1]], [[8, 6, 5, 10, 0, 2, 1]], [[10, 5, 4, 7, 9]], [[-2, 0, -1, 2, 1, 8, 6, 5, 4]], [[1, 2, 4, 12, 7, 5, 8]], [[1, 2, 3, 10, 4, 11, 5, 6, 9, 8]], [[1, 2, 12, 7, 0, 8]], [[4, 7, 0]], [[3, 4, 5, 6, 8]], [[1, 2, 4, 0, -2, 7, 6, 12]], [[5, 9, 6, 10]], [[10, 2, 4, 6, 9]], [[-2, 2, 5, 4, 7, 6, 8]], [[1, 2, 6, 0, 8]], [[1, 3, 5, 8, 2, 9]], [[9, 8, 7, 6, -2, 1]], [[3, 5, 8, 11, 10]], [[1, 4, 7, 0]], [[1, 3, 5, 6, 8, 2]], [[1, 12, 2, -2, 7, 9, 6]], [[3, 5, 7, 4, 2, 9]], [[9, 8, 7, 11, -2, 1]], [[10, 5, 12, 4, 6, 9]], [[1, 3, 7, 6, 9]], [[9, 1, 12, 6, 11, 5, 8, 4, 3]], [[12, 6, 5, 4, 3, 1]], [[1, 4, -3, 5, -1]], [[8, 6, 3, 4, 1]], [[2, 3, 5, 12, 7, 9, 8]], [[3, 2, 6, 7, 1, 4]], [[8, 7, 0, 2]], [[9, 1, 6, 5, 8, 4, 3]], [[3, 7, 0, 2]], [[1, 3, 5, 7, 11, 2, 6, 8, 10, 12]], [[2, 3, -3, 9, -2, 7, 10, 8]], [[1, 2, 4, -2, 7, -3, 8, 9]], [[4, 1, 5, 7, 6, 8, 11, 12, 10]], [[7, 5, 3, 12]], [[8, 5, 11, 0, 2]], [[10, 1, 2, -2, 7, 9, 8, 5]], [[5, 3, 2, 6, 9, 7, 1, 12, 8, 4]], [[-2, 1, 5, 3, 7, 6, 9, 8]], [[8, 1, 5, 10, 0, 2]], [[9, 7, 6, -2, 1]], [[1, 2, 4, 5, 6, -3, -2]], [[10, 1, -1, 11, 4, -2, 7, 9, 8]], [[9, 7, 6, -1, 1]], [[7, 6, 5, 11, 3, 12]], [[1, 3, 2, 5, 8]], [[1, 9, 3, 5, -2, 6, 11]], [[7, 8, 1, 5, 10, 0, 2]], [[11, 4, 7, -1, 8]], [[7, 5, 3, 9]], [[5, 7, 8, 11, 12, 4]], [[1, 2, 12, 4, 7, 9]], [[7, 6, 5, 4, 3, -2, 2, 1]], [[5, 3, 11, 6, 7, 1, 4]], [[1, 2, 3, 4, 5, -1, 9, 8]], [[4, 7, 6, 3, 11, -2]], [[1, 3, 4, 5, -1, 6, 2, 11, 8]], [[1, 0, 3, 5, 4, 7, 6, 9]], [[0, 2, 5, 4, 7, 6]], [[10, 5, 7, 6, 9]], [[1, 2, 4, 12, 7, 10, 8]], [[5, 2, 7, 11, 10, 1, 4, 9]], [[10, 1, 2, -2, 7, 9, 8]], [[1, 2, 7, 4, 5, -2, 6, 11, 8, 12]], [[1, 4, 5, 7, 0]], [[10, 1, 2, -2, 6, 9, 8]], [[1, 3, 5, 7, 6, 8, 11, 12, 4]], [[1, 2, 4, 5, 6, 7, -1]], [[0, 5, 7, 1, 8, 4]], [[1, 7, 0]], [[1, 3, 7, 12, 6, 9]], [[2, 4, 9, 0, 8]], [[3, 2, 9, 1, 8, 4]], [[8, 7, -2, 5, 3, 4, 1]], [[1, 2, 4, -2, 7, 0, 10, 8]], [[-48, 1, 12, 11, -1, 51, 97, -50]], [[8, 7, 5, 11, 3, 0, 2]], [[3, 7, 6, 9]], [[-2, 0, 2, 1, 8, 7, 6, 5, 97]], [[7, 4, 1, 5, 10, 0, 2]], [[7, 10, 5, 3, 4, 1]], [[3, 7, 2]], [[5, 2, 7, 10, 1, 4, 97]], [[1, 9, 3, 4, -50, -2, 6, 11, 8]], [[7, -1, 6, 5, 3, 12]], [[9, 8, 6, -2, 1]], [[1, 12, 2, -3, 7, 9, 6]], [[3, 6, 10, 11, 12, 9]], [[10, 1, 2, 5, -2, 6, 7, 9, 8]], [[1, 5, 7, 6, 9]], [[1, 12, 3, 4, 7]], [[1, -2, 3, 5, 6, 8, 2]], [[9, 1, 12, 6, 11, 5, 7, 4, 3]], [[10, 7, 0, 9]], [[5, 7, 9, 10, 0, 8]], [[10, 7, 5, 11, 3, 12]], [[1, 2, 4, 0, -2, 6, 12]], [[1, -2, 5, 6, 8, 2]], [[3, 5, 4, 7, 6, 9, 8]], [[-2, 0, 2, 1, 8, 7, 6, 5, -48, 4]], [[2, 3, 5, 12, 6, 9, 8]], [[1, 3, -48, 7, 9, 11, 2, 4, 6, 8, 10, 12]], [[8, 7, 6, 5, -2, 3, 1]], [[10, 5, 7, 9]], [[3, 2, 5, 4, 7, 9, 8]], [[1, 2, 3, 4, 5, -2, 9, 0]], [[9, 6, 5, 10, 0, 2, 1]], [[10, 3, 2, -2, 6, 7, 9, 8]], [[10, 1, 2, 7, 9, 8]], [[10, 1, 2, 9, 6, 8]], [[5, 2, -1, 10, 1, 8, 4, 9]], [[0, 5, 2, 7, 1, 8]], [[1, 6, 5, 8, 7, 4]], [[11, 97, 4, 7, -1, 8, 2]], [[7, 5, 3, 0, 2, 1]], [[2, 5, 97, 7, 6, 9, 8]], [[3, 7, 4, 97, 5, 2]], [[1, 3, -3, 2, 5, 8]], [[7, 5, 3, 2, 1]], [[8, 6, 3, 4, 5, 1]], [[10, 1, 2, 5, 6, 7, 9, 8]], [[8, 0]], [[9, 1, 6, 5, 4, 3]], [[9, 1, 2, 5, 8, 7, 4, 3]], [[1, 3, 2, 5, 4]], [[3, 5, 7, 4, 9]], [[5, 7, 3, 9, 10, 1, 8, 4]], [[7, 6, 5, 3, 9]], [[1, 51, 2, 5, 8]], [[7, 4, 97, 5, 2]], [[3, 2, 9, 1, 8]], [[1, 3, 5, 7, 6, 8, 11, 13, 4]], [[52, -48, 1, 12, 11, -1, 51, 97, -50]], [[10, 0, 9]], [[-48, 1, 3, 4, 7, 0]], [[11, 3, 7, -1, 8]], [[5, 3, 13, 2, 6, 7, 1, 8, 4]], [[-2, 0, -1, 2, 8, 6, 5, 4, 1]], [[5, 2, 10, -48, 1, 8, 4]], [[1, 3, 2, 5, 4, 7, 9, 11, 8]], [[9, 0, 1, 2, 12, 6, 5, 7, 4, 3]], [[1, 51, 5, 8]], [[2, 3, 4, 5, -2, 9, 8]], [[10, 1, 2, 9, 6]], [[0, 5, 2, 7, 1, 4]], [[2, 3, -3, 9, 10, 8]], [[10, 1, 6, 2, 5, -2, 8, 7, 4, 3]], [[5, 7, 8, 11, 4]], [[8, 6, 3, -48, 4, 5, 1]], [[1, 2, 3, 4, 5, -2, 10, 0]], [[8, 7, 5, 10, 3, 2, 1]], [[8, 7, 5, 3, 10]], [[12, 2, 10, 3, 11, 5, 6, 9, 8]], [[1, 2, 7, 4, 5, -2, 6, 11, 9, 12]], [[1, 2, 3, 4, 5, -2, 6, 8]], [[2, 3, 9, -2, 7, 10, 8]], [[3, 5, 7, 4, 2, 10, 9]], [[8, 9, 7, 5, 11, 0, 2]], [[1, 2, 5, 9, 8]], [[7, 5, 4, 3, 2, 0, 1]], [[-2, 5, 6, 8, 2]], [[7, 5, 10, 0, 2]], [[10, 1, -1, 11, 3, -2, 7, 9, 8]], [[1, 3, 5, 7, 6, 8, 13, 4]], [[10, 1, 9, 6, 8]], [[3, 2, 5, 7, 1, 4]], [[4, 7, -1, 8]], [[10, 0]], [[1, 2, 7, 9, 8]], [[13, 8, 0]], [[1, 5, 3, 6, 7, 9, 8]], [[1, 12, 3, 6, 7, 9, 8]], [[4, 7, 6, 11, -2]], [[12, 1, 9, 3, 2, 5, 4, 8]], [[10, 2, 9, 6]], [[5, -50, 8, 6, 11, 10]], [[10, 9, 8, 7, 5, 4, 3, 2, 1]], [[5, 3, 13, 2, 6, 51, 7, 1, 8, 4]], [[1, 3, 5, 4, 7, 6, 51]], [[1, 9, 3, 4, -50, -2, 6, 11]], [[2, 3, 9, 10, 8]], [[1, 3, 7, 4, 2, 9]], [[1, 0]], [[11, 51, 1, 3, 7, 0]], [[8, 4, 11, 0, 2]], [[-2, 0, -1, 2, 1, 8, 5, 4]], [[7, -48, 6, 5, 3, 9]], [[2, 9, 12, 10, 8]], [[1, 2, 0, 3, 4, 5, 6, 11, 8]], [[3, 5, 7, 11, 9, 4]], [[1, 3, 5, -2, 6, 2, 11, 8]], [[9, 8, 11, -2, 1]], [[1, 2, 3, 4, 5, 6, 10]], [[3, 4, 7, 2]], [[3, 7, 0]], [[1, -50, 12, 2, -2, 7, 9, 6]], [[9, 1, 12, 6, 5, 7, 4, 3]], [[3, 5, 7, -2, 8, 11, 12, 9]], [[12, 2, 5, 4, 3, 1]], [[-2, 2, 6, 9, 4]], [[1, 2, 4, 0, -2, 6]], [[1, 2, 0, 3, 4, 5, -3, 9, 6, 11, 8]], [[1, 13, 2, 5, 8]], [[8, 7, 0, 3, 10]], [[3, 4, 6, 8]], [[5, 3, 2, 9, 11, 4]], [[7, 5, 11, 3, 2, 1]], [[10, 1, 2, 9, 5, 6, 8]], [[0, 5, 2, 7, 1, 12]], [[0, 2, 1, 3, 10, 7, 6, 4]], [[1, 4, 0, -2, 7, 9, 8]], [[9, 1, 5, 4, 3]], [[12, 0, 97, 7, 3, 2, 9, 5, 4, 8]], [[2, 4, 5, -2, 9, 8]], [[10, 5, 1, 2, 4, -2, 7, 9, 8]], [[1, 2, 4, 12, 10, 8]], [[10, 2, 7]], [[1, 13, 2, 3, 4, 5, -2, 6, 8]], [[-48, 3, 4, 7, 0]], [[4, 1, 5, 9, 7, 6, 8, 11, 12, 10]], [[9, 1, 12, 6, 5, 7, 3]], [[8, 7, 6, 4, 3, 2, 1]], [[1, 2, 3, 4, 5, -2, 12, 6, 8]], [[-1, 12, 2, 5, 4, 3, 1]], [[11, 0, 9]], [[10, 0, 3, 9, 6, 8]], [[2, 3, 10, 8]], [[5, 7, 10, 8, 11, 12, 4]], [[4, 7, 5, 11, 3, 1]], [[1, 4, 51, 7, 9, 8]], [[-48, 1, 3, 4, 6, 0]], [[51, 13, 2, 3, 4, 5, -2, 6, 8]], [[5, 3, 11, 6, 7, 2, 1, 4]], [[10, 2, -2, 7, 9, 8, 5]], [[1, -2, 7, 9]], [[1, 2, 6, 8]], [[4, 7, 5, 11, -50, 1]], [[3, 2, 6, 7, 1, 8, 51, 4]], [[10, 1, 2, 9]], [[1, 3, 5, 7, 6, 8, 13]], [[9, 0, 1, 12, 6, 8, 7, 4, 3]], [[1, 7, 2, 4, 5, 6, 8]], [[-2, 2, 9, 4]], [[2, 3, -3, 9, 10]], [[8, 7, 5, 3, 9]], [[10, 9, 8, 7, 6, 5, 4, 2, 1]], [[10, 9, 8, 7, 6, 4, 3, 2, 1]], [[8, 7, 5, 3, 52, 10, -50, 0, 2]], [[2, 5, 97, 7, 3, 9, 8]], [[3, 7, 2, 9, -2, 1, 8]], [[8, 7, 97, 9]], [[2, 7, 9, 10, 1, 8]], [[4, 7, 5, -50, 1, 11]], [[5, 8, 7, 6, 10]], [[0, 13, 7, 5, -2, 6, 11, 8, 12]], [[2, 7, 1, 0]], [[1, 0, -2, 7, 9, 8]], [[-2, 2, 4, 7, 6, 8]], [[9, 5, -50, 2, 7, 10, 1, 8, 4]], [[1, 3, -3, 2, 8]], [[4, 5, 7, 6, 8, 9]], [[4, 5, 11, 1]], [[1, 7, 8]], [[2, 5, 4, 7, 6, 9]], [[-2, 0, 2, 8, 7, 6, 5, 4]], [[12, 1, 9, 2, 5, 4, 8]], [[9, 8, 10, 7, 5, 4, 3, 2, 1]], [[2, 4, 5, -2, 9]], [[13, 2, 5, 8]], [[1, 2, 4, 5, 6, 7]], [[8, 7, 6, 5, -2, -50, 3, 0, 1]], [[4, 7, 3, 11, -2]], [[1, 4, -3, 5]], [[6, 3, 11, -2]], [[3, 2, 6, 7, 12, 4]], [[5, 2, 7, 10, 4, 9]], [[10, 3, 2, -2, -50, 6, 7, 9, 8]], [[-1, 12, 5, 4, 3, 1]], [[8, 7, 5, 3, -1, 2, 1]], [[3, 2, 4, 5, 6, -3, -2]], [[4, 1, 5, -50, 6, 11, 7]], [[3, 7, 1]], [[3, 7, 4, 2, 9, -3, 1, 8]], [[1, 3, 5, 7, 6, 8, 12, 4]], [[3, 7, 1, 2]], [[9, 1, 6, 11, 5, 8, 4, 3]], [[0, 1, 6, 2, 8, 7, 4, 3]], [[1, 3, 5, 7, 11, 2, 6, 8, 10]], [[2, 10, 13]], [[10, 5, 4, 7, 6]], [[4, 5, 6, 8, 11, 9]], [[2, 3, 9, 53, 10, 8]], [[1, 3, 2, -3, 9, -2, 7, 10, 8]], [[1, 2, 0, 12, 3, 4, 5, 6, 11, 8]], [[7, 4, 97, 5, 11]], [[3, 7]], [[1, 2, 4, 7, 9, 3, 8]], [[5, 7, 10, 8, 4]], [[10, 5, 4, 6]], [[-2, 0, 2, 1, 3, 8, -1, 7, 6, 5, 4]], [[9, 6, 5, 10, 0, 1]], [[8, 7, -2, 5, 3, 1]], [[4, 5, 7, 6, 8, -3]], [[-2, 6, 8, 2]], [[1, 2, 4, -2, 0, 10, 8]], [[1, 4, 51, 7, 9, 53, 8]], [[4, 7, -3, 3, 11, -2]], [[4, 7]], [[4, 6, 11, 8]], [[10, 9, 8, 7, 6, 5, 4, 3, 51, 1]], [[1, -2, 7, 9, 8]]]
    results = [True, True, False, False, True, True, True, True, False, True, False, False, False, True, False, True, False, False, False, True, True, True, True, True, False, False, False, False, True, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True, True, True, False, True, True, True, False, True, False, True, False, False, False, True, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, False, False, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, True, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(move_one_ball)