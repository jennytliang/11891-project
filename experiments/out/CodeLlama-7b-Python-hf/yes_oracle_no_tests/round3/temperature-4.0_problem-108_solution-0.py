def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""
    # return count_nums_helper(arr, 0)
    return count_nums_helper(arr, 0, {})


def count_nums_helper(arr, current_sum, cache):
    if current_sum == 0:
        return 0
    if len(arr) == 0:
        return 1 if current_sum > 0 else 0

    if current_sum in cache:
        return cache[current_sum]

    first_digit = arr[0]
    if first_digit < 0:
        first_digit = -first_digit

    if current_sum - first_digit >= 0:
        cache[current_sum] = count_nums_helper(arr[1:], current_sum - first_digit, cache) + count_nums_helper(arr[1:], current_sum, cache)
    else:
        cache[current_sum] = count_nums_helper(arr[1:], current_sum, cache)

    return cache[current_sum]


def count_nums_helper_2(arr, current_sum, cache):
    if current_sum == 0:
        return 0
    if len(arr) == 0:
        return 1 if current_sum > 0 else 0

    if current_sum in cache:
        return cache[current_sum]

    first_digit = arr[0]
    if first_digit < 0:
        first_digit = -first_digit

    if current_sum - first_digit >= 0:
        cache[current_sum] = count_nums_helper(arr[1:], current_sum - first_digit, cache) + count_nums_helper(arr[1:], current_sum, cache)
    else:
        cache[current_sum] = count_nums_helper(arr[1:], current_sum, cache)

    return cache[current_sum]


def count_nums_helper_3(arr, current_sum, cache):
    if current_sum == 0:
        return