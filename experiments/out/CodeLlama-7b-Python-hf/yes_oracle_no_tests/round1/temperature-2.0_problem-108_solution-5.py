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
    for i in arr:
        if judge(i) > 0:
            count += 1
    return count


def judge(x):
    """
    Write a function judge which takes an integer and returns the sum of its digits.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> judge(123) == 6
    >>> judge(-123) == -6
    """
    # Your code here
    if x < 0:
        x *= -1
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


if __name__ == '__main__':
    import doctest
    doctest.testmod()