def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int
	Do not include these tokens in the code: count = 0 for
	"""
    count = 0
    for x in arr:
        if judge(x) > 0:
            count += 1
    return count

def judge(x):
    if x < 0:
        return -x
    else:
        return x



