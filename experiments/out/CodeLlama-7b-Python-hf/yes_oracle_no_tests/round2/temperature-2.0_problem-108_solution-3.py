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
    c = 0
    for i in arr:
        if judge(i) == 1:
            c += 1
    return c


def judge(x):
    s = str(x)
    for i in s:
        if int(i) > 0:
            return 1
        else:
            return -1


print(count_nums([-1, 11, -11]))
