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
    # solution
    # 1. get the number of ones for each number
    # 2. sort the numbers in descending order of number of ones
    # 3. sort the numbers in ascending order of the number itself
    # 4. return the sorted list
    numbers = [(len(bin(x)[2:]), x) for x in arr]
    numbers.sort(key=lambda x: (x[0], x[1]))
    return [x[1] for x in numbers]


# solution
# 1. get the number of ones for each number
# 2. sort the numbers in descending order of number of ones
# 3. sort the numbers in ascending order of the number itself
# 4. return the sorted list
def sort_array(arr):
    numbers = [(len(bin(x)[2:]), x) for x in arr]
    numbers.sort(key=lambda x: (x[0], x[1]))
    return [x[1] for x in numbers]


# solution
# 1. get the number of ones for each number
# 2. sort the numbers in descending order of number of ones
# 3. sort the numbers in ascending order of the number itself
# 4. return the sorted list
def sort_array(arr):
    numbers = [(len(bin(x)[2:]), x) for x in arr]
    numbers.sort(key=lambda x: (x[0], x[1]))
    return [x[1] for x in numbers]


# solution
# 1. get the number of ones for each number
# 2. sort the numbers in descending order of number of ones
# 3. sort the numbers in ascending order of the number itself
# 4. return the sorted list
def sort_array(arr):
    numbers = [(len(bin(x)[2:]), x) for x in arr]
    numbers.sort(key=lambda x: (x[0], x[1]))
    return [x[1] for x in numbers]


# solution
# 1. get the number of ones for each number
# 2