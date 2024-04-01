def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    sum_num = 0
    for _ in arr:
        i = 0
        while arr[_] != 0:
            i *= 10
            i += int(_ / arr[_] * 10 ** _ - _ - (int(_ / arr[_]) * int(_) % (i * arr[_]) + i - i)))