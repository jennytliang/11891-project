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
    # Your code here
    count = 0
    for x in arr:
        count += judge(x)
    return count

def judge(x):
    if x < 0:
        x = -x
    if x == 0:
        return 0
    if x % 10 > 0:
        return 1
    else:
        return judge(x // 10)


def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Do not use any loops.
    """
    return sum(judge(x) for x in arr)


def judge(x):
    if x < 0:
        x = -x
    if x == 0:
        return 0
    if x % 10 > 0:
        return 1
    else:
        return judge(x // 10)


def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
    Do not use any loops.
    """
    return sum(judge(x) for x in arr)
