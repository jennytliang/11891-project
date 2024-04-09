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
    count = 0
    for num in arr:
        if judge(num):
            count += 1
    return count

def judge(x):
    result = 0
    if x < 0:
        x = -x
    
    while x != 0:
        result += x % 10
        x = x // 10

    return result > 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()